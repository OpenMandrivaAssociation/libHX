%define major	28
%define libname %mklibname HX %{major}
%define devname %mklibname HX -d

Summary:	A library for common data structures and low level operations
Name:		libHX
Version:	3.13
Release:	7
Group:		System/Libraries
License:	GPLv3+ and LGPLv2+
Url:		http://libhx.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/libhx/%{name}/%{version}/libHX-%{version}.tar.xz
Source1:	http://downloads.sourceforge.net/project/libhx/%{name}/%{version}/libHX-%{version}.tar.xz.asc

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
Group:		System/Libraries
Summary:	General-purpose library

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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
# /sbin/mount.crypt from pam_mount uses libHX
%configure2_5x \
	--disable-static \
	--libdir=/%{_lib} \
	--with-pkgconfigdir=%{_libdir}/pkgconfig
%make

%install
%makeinstall_std

%files -n %{libname}
/%{_lib}/libHX.so.%{major}*

%files -n %{devname}
%doc doc/*
%doc %{_datadir}/doc/libhx/libHX_Documentation.pdf
%{_includedir}/*
/%{_lib}/*.so
%{_libdir}/pkgconfig/libHX.pc

