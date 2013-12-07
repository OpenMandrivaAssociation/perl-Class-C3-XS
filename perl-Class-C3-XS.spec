%define upstream_name	 Class-C3-XS
%define upstream_version 0.13

Summary:	XS speedups for Class::C3 
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:	perl-devel

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
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorarch}/Class
%{perl_vendorarch}/auto/Class
%{_mandir}/man3/*

