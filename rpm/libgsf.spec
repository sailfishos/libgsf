Name:       libgsf
Summary:    GNOME Structured File library
Version:    1.14.52
Release:    1
License:    LGPLv2
URL:        https://github.com/sailfishos/libgsf
Source0:    %{name}-%{version}.tar.xz
Patch0:     disable-gtkdoc.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.16
BuildRequires:  bzip2-devel
BuildRequires:  gettext

%description
A library for reading and writing structured files (eg MS OLE and Zip)

%package devel
Summary:    Support files necessary to compile applications with libgsf
Requires:   %{name} = %{version}-%{release}

%description devel
Libraries, headers, and support files necessary to compile applications
using libgsf.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
echo "EXTRA_DIST = missing-gtk-doc" > gtk-doc.make
sh autogen.sh

%configure --disable-static \
    --disable-gtk-doc \
    --without-python

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%find_lang libgsf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libgsf.lang
%license COPYING
%{_libdir}/libgsf-1.so.*
%{_bindir}/gsf-office-thumbnailer
%{_datadir}/thumbnailers/gsf-office.thumbnailer

%files devel
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_libdir}/libgsf-1.so
%{_libdir}/pkgconfig/libgsf-1.pc
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/gsf
%{_mandir}/man1/gsf.1.gz
%{_mandir}/man1/gsf-vba-dump.1.gz
%{_mandir}/man1/gsf-office-thumbnailer.1.gz

