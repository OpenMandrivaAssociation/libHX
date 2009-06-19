%define major 18
%define libname %mklibname HX %{major}
%define develname %mklibname HX -d

Name:           libHX
Version:        2.7
Release:        %mkrel 1
Summary:        A library for common data structures and low level operations
Group:          System/Libraries
License:        GPLv3+ and LGPLv2+
URL:            http://jengelh.medozas.de/projects/libHX/
Source0:        http://jengelh.medozas.de/files/libHX/libHX-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%clean
rm -rf %{buildroot}


%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif


%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*


%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libHX.pc
%{_datadir}/doc/libhx/libHX_Documentation.pdf
