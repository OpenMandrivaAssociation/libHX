%define major 10
%define libname %mklibname HX %{major}
%define develname %mklibname HX -d

Name:           libHX
Version:        1.10.2
Release:        %mkrel 1
Summary:        General-purpose library

Group:          System/Libraries
License:        GPL
URL:            http://jengelh.hopto.org/f/libHX/
Source0:        http://jengelh.hopto.org/f/libHX/libHX-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  perl gcc


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


%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{develname} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
cp -a t examples


%build
%configure2_5x --disable-static
%make
rm examples/Makefile*

%install
rm -rf %{buildroot}
%makeinstall_std
#make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc LICENSE.LGPL2 LICENSE.LGPL3 LICENSE.GPL3
%{_libdir}/*.so.*


%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/* examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libHX.pc
