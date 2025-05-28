%define major	32
%define libname %mklibname HX
%define oldlibname %mklibname HX 28
%define devname %mklibname HX -d

Summary:	A library for common data structures and low level operations
Name:		libHX
Version:	4.27
Release:	1
Group:		System/Libraries
License:	GPLv3+ and LGPLv2+
Url:		https://inai.de/projects/libhx/
Source0:	https://inai.de/files/libhx/libHX-%{version}.tar.xz
Source1:	https://inai.de/files/libhx/libHX-%{version}.tar.asc
BuildSystem:	autotools

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
# Renamed after 5.0
%rename %{oldlibname}

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

%files -n %{libname}
%{_libdir}/libHX.so.%{major}*

%files -n %{devname}
%doc doc/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libHX.pc
