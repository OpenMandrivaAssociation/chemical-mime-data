Summary:	Support for chemical/* MIME types
Name:		chemical-mime-data
Version:	0.1.94
Release:	17
Group:		System/Libraries
License:	LGPLv2.1
Url:		http://sourceforge.net/projects/chemical-mime/
Source0:	http://dl.sourceforge.net/chemical-mime/%{name}-%{version}.tar.bz2
Patch0:		chemical-mime-data-0.1.94-rosa-rsvg.patch
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	librsvg
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	xsltproc
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
Requires:	shared-mime-info
Requires:	hicolor-icon-theme

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
 
%description devel
The pkgconfig for %{name}.

%prep
%setup -q
sed -i -e '/^libdir/d' chemical-mime-data.pc.in
%apply_patches
# required for patch0
autoreconf

%build
export RSVG=%{_bindir}/rsvg-convert
%configure2_5x \
	--disable-update-database \
	--without-gnome-mime \
	--without-pixmaps
%make

%install
%makeinstall_std
cp -pR %{buildroot}%{_docdir}/%{name} __docs
rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING HACKING NEWS README THANKS TODO
%doc __docs/*
%{_iconsdir}/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_iconsdir}/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/mimelnk

%files devel
%{_datadir}/pkgconfig/chemical-mime-data.pc

