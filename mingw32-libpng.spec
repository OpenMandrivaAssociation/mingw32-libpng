%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-libpng
Version:        1.2.35
Release:        %mkrel 3
Summary:        MinGW Windows Libpng library

License:        zlib
URL:            https://www.libpng.org/pub/png/
Source0:        ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.bz2
Patch0:         libpng-multilib.patch
Patch1:         libpng-pngconf.patch

Group:          Development/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 40
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

Requires:       pkgconfig

%description
MinGW Windows Libpng library.


%prep
%setup -q -n libpng-%{version}
%patch0 -p1
%patch1 -p1

%build
%{_mingw32_configure}
make


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%{_mingw32_libdir}/libpng.a

# No need to distribute manpages which appear in the Fedora
# native packages already.
rm -rf $RPM_BUILD_ROOT%{_mingw32_mandir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc ANNOUNCE CHANGES KNOWNBUG LICENSE README TODO Y2KINFO
%{_mingw32_bindir}/libpng-3.dll
%{_mingw32_bindir}/libpng-config
%{_mingw32_bindir}/libpng12-0.dll
%{_mingw32_bindir}/libpng12-config
%{_mingw32_includedir}/libpng12
%{_mingw32_includedir}/png.h
%{_mingw32_includedir}/pngconf.h
%{_mingw32_libdir}/libpng.dll.a
%{_mingw32_libdir}/libpng.la
%{_mingw32_libdir}/libpng12.a
%{_mingw32_libdir}/libpng12.dll.a
%{_mingw32_libdir}/libpng12.la
%{_mingw32_libdir}/pkgconfig/libpng.pc
%{_mingw32_libdir}/pkgconfig/libpng12.pc
