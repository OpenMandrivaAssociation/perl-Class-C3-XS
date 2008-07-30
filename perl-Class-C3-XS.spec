%define module	Class-C3-XS
%define name	perl-%{module}
%define version	0.08
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	XS speedups for Class::C3 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This contains XS performance enhancers for Class::C3 version 0.16 and higher.
The main Class::C3 package will use this package automatically if it can find
it. Do not use this package directly, use Class::C3 instead.

The test suite here is not complete, although it does verify a few basic
things. The best testing comes from running the Class::C3 test suite *after*
this module is installed.

This module won't do anything for you if you're running a version of Class::C3
older than 0.16. (It's not a dependency because it would be circular with the
optional dep from that package to this one).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/Class
%{perl_vendorarch}/auto/Class
%{_mandir}/*/*

