%define upstream_name       Config-Model-CursesUI
%define upstream_version    1.104

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Curses interface for Config::Model
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Module::Build)
BuildRequires: perl(Config::Model)
BuildRequires: perl(Curses::UI)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This class provides a the Curses::UI manpage interface to configuration
data managed by the Config::Model manpage.

IMPORTANT: Once the CursesUI object is created, STDOUT and STDERR are
managed by the Curses interface, so all print and warn will not work as
expected.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*


