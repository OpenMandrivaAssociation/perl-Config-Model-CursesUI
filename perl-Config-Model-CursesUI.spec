%define upstream_name       Config-Model-CursesUI
%define upstream_version    1.104

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Summary:	Curses interface for Config::Model
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Config::Model)
BuildRequires:	perl(Curses::UI)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This class provides a the Curses::UI manpage interface to configuration
data managed by the Config::Model manpage.

IMPORTANT: Once the CursesUI object is created, STDOUT and STDERR are
managed by the Curses interface, so all print and warn will not work as
expected.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.104.0-2mdv2011.0
+ Revision: 657479
- add br
- rebuild for updated spec-helper

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.104.0-1
+ Revision: 641322
- update to new version 1.104

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.103.0-1mdv2011.0
+ Revision: 393055
- import perl-Config-Model-CursesUI


* Mon Jul 06 2009 cpan2dist 1.103-1mdv
- initial mdv release, generated with cpan2dist

