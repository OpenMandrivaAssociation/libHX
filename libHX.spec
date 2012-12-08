%define major 28
%define libname %mklibname HX %{major}
%define develname %mklibname HX -d

Name:           libHX
Version:        3.13
Release:        1
Summary:        A library for common data structures and low level operations
Group:          System/Libraries
License:        GPLv3+ and LGPLv2+
URL:            http://libhx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/libhx/%{name}/%{version}/libHX-%{version}.tar.xz
Source1:        http://downloads.sourceforge.net/project/libhx/%{name}/%{version}/libHX-%{version}.tar.xz.asc

%description
A library for:
- A+R/B trees to use for lists or maps (associative arrays)
- Deques (double-ended queues) (Stacks (LIFO) / Queues (FIFOs))
- platform independent opendir-style directory access
- platform independent dlopen-style shared library access
- auto-storage strings with direct access
- command line option (argv) parser
- shell-style config file parser
- platform independent random number generator with transparent
  /dev/urandom support
- various string, memory and zvec ops

%package -n %{libname}
Group: System/Libraries
Summary: General-purpose library
Obsoletes: %{name} < 1.17-2

%description -n %{libname}
- A+R/B trees to use for lists or maps (associative arrays)
- Deques (double-ended queues) (Stacks (LIFO) / Queues (FIFOs))
- platform independent opendir-style directory access
- platform independent dlopen-style shared library access
- auto-storage strings with direct access
- command line option (argv) parser
- shell-style config file parser
- platform independent random number generator with transparent
  /dev/urandom support
- various string, memory and zvec ops

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
# /sbin/mount.crypt from pam_mount uses libHX
%configure2_5x --disable-static --libdir=/%{_lib} --with-pkgconfigdir=%{_libdir}/pkgconfig
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
/%{_lib}/*.so.%{major}*

%files -n %{develname}
%doc doc/*
%{_includedir}/*
/%{_lib}/*.so
%{_libdir}/pkgconfig/libHX.pc
%{_datadir}/doc/libhx/libHX_Documentation.pdf


%changelog
* Mon Jul 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.13-1
+ Revision: 811445
- update to 3.13
- move libHX.so to /%%{_lib}/ because it is needed for /sbin/mount.crypt from pam_mount

* Fri Dec 16 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.12.1-1
+ Revision: 743153
- added new tarball and signature
- update to 3.12.1

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 3.10.1-2
+ Revision: 662343
- mass rebuild

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 3.10.1-1
+ Revision: 652019
- new verison 3.10.1

* Thu Dec 02 2010 Funda Wang <fwang@mandriva.org> 3.8-1mdv2011.0
+ Revision: 604653
- update to new version 3.8

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 3.6-1mdv2011.0
+ Revision: 572567
- update to new version 3.6

* Wed Aug 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.5-1mdv2011.0
+ Revision: 565744
- new version

* Thu Apr 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.4-1mdv2010.1
+ Revision: 533228
- update to new version 3.4

* Fri Jan 22 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.3-1mdv2010.1
+ Revision: 494878
- new version

* Tue Nov 17 2009 Frederik Himpe <fhimpe@mandriva.org> 3.2-1mdv2010.1
+ Revision: 467025
- update to new version 3.2

* Thu Sep 24 2009 Frederik Himpe <fhimpe@mandriva.org> 3.1-1mdv2010.0
+ Revision: 448399
- update to new version 3.1

* Mon Aug 31 2009 Frederik Himpe <fhimpe@mandriva.org> 3.0.1-1mdv2010.0
+ Revision: 423033
- Update to new version 3.0.1
- Fix URL

* Sat Aug 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.0-1mdv2010.0
+ Revision: 422156
- new version

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-1mdv2010.0
+ Revision: 393856
- new version

* Fri Jun 19 2009 Funda Wang <fwang@mandriva.org> 2.7-1mdv2010.0
+ Revision: 387375
- New version 2.7

* Tue Feb 17 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5-1mdv2009.1
+ Revision: 342153
- Update to new version 2.5

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 2.3-1mdv2009.1
+ Revision: 332744
- New upstream release

* Fri Jan 02 2009 Frederik Himpe <fhimpe@mandriva.org> 2.2-1mdv2009.1
+ Revision: 323415
- Update to new version 2.2 (new major)

* Sat Dec 27 2008 Frederik Himpe <fhimpe@mandriva.org> 2.1-1mdv2009.1
+ Revision: 319867
- Update to new version 2.1 (new major)

* Wed Nov 19 2008 Funda Wang <fwang@mandriva.org> 1.28-1mdv2009.1
+ Revision: 304371
- new version 1.28

* Mon Oct 13 2008 Frederik Himpe <fhimpe@mandriva.org> 1.26-1mdv2009.1
+ Revision: 293348
- Better summary
- Update to new version 1.26
- Use %%{buildroot} instead of $RPM_BUILD_ROOT
- Fix libification, don't package standard licenses

* Sun Sep 07 2008 Funda Wang <fwang@mandriva.org> 1.25-1mdv2009.0
+ Revision: 282265
- New version 1.25
- new major 13->14

* Fri Sep 05 2008 Frederik Himpe <fhimpe@mandriva.org> 1.23-1mdv2009.0
+ Revision: 281353
- Update to new version 1.23

* Thu Jul 17 2008 Funda Wang <fwang@mandriva.org> 1.22-1mdv2009.0
+ Revision: 236673
- New version 1.22

* Sat Jun 21 2008 Buchan Milne <bgmilne@mandriva.org> 1.18-1mdv2009.0
+ Revision: 227823
- New version 1.18

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 18 2008 Funda Wang <fwang@mandriva.org> 1.17-2mdv2009.0
+ Revision: 208572
- fix libname under x86_64

* Sun May 18 2008 Funda Wang <fwang@mandriva.org> 1.17-1mdv2009.0
+ Revision: 208571
- New version 1.17

* Wed Feb 13 2008 Adam Williamson <awilliamson@mandriva.org> 1.10.2-2mdv2008.1
+ Revision: 166935
- devel package should provide %%name-devel, not %%develname...

* Fri Jan 18 2008 Jérôme Soyer <saispo@mandriva.org> 1.10.2-1mdv2008.1
+ Revision: 154581
- New release

* Thu Jan 17 2008 Jérôme Soyer <saispo@mandriva.org> 1.10.1-1mdv2008.1
+ Revision: 154080
- import libHX


