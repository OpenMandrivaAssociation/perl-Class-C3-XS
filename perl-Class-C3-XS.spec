%define upstream_name	 Class-C3-XS
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:	XS speedups for Class::C3 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-5mdv2012.0
+ Revision: 765083
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-4
+ Revision: 763526
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-3
+ Revision: 676909
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 555226
- rebuild

* Fri Sep 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 448607
- update to 0.13

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 403005
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2010.0
+ Revision: 370032
- update to new version 0.11

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.08-4mdv2009.0
+ Revision: 255893
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.08-2mdv2008.1
+ Revision: 151854
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 48053
- import perl-Class-C3-XS


* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
- initial mdv release
