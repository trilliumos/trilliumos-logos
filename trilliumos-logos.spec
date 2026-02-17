# Package must be arch specific because there are deps on arm that are missing
%global codename jasper
%global debug_package %{nil}

Name:       trilliumos-logos
Version:    100.4
Release:    99%{?dist}
Summary:    trilliumOS related icons and pictures

Group:      System Environment/Base
URL:        https://github.com/trilliumos/branding

Source0:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

License:    Licensed only for approved usage, see COPYING for details.

Obsoletes:  %{name} < 90.4-1
Obsoletes:  redhat-logos < 90.1-1
Obsoletes:  rocky-logos < 90
Provides:   system-logos = %{version}-%{release}
Provides:   redhat-logos = %{version}-%{release}

Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5

# No mixing logos
Conflicts:  centos-logos
Conflicts:  almalinux-logos
Conflicts:  oracle-logos
Conflicts:  rocky-logos

# All build requires
BuildRequires: hardlink
BuildRequires: make

# All requires
Requires(post): coreutils

%description
Licensed only for approved usage, see COPYING for details.

%package httpd
Summary: trilliumOS related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Provides: redhat-logos-httpd = %{version}-%{release}
Provides: system-logos(httpd-logo-ng)
BuildArch: noarch

%description httpd
Licensed only for approved usage, see COPYING for details.

%package ipa
Summary: trilliumOS related icons and pictures used by FreeIPA
Provides: system-logos-ipa = %{version}-%{release}
Provides: redhat-logos-ipa = %{version}-%{release}
BuildArch: noarch

%description ipa
Licensed only for approved usage, see COPYING for details.

%package -n trilliumos-backgrounds
Summary: trilliumOS related desktop backgrounds
BuildArch: noarch

Obsoletes: redhat-logos < 80.1-2
Provides:  system-backgrounds = %{version}-%{release}
Requires:  redhat-logos = %{version}-%{release}

%description -n trilliumos-backgrounds
Licensed only for approved usage, see COPYING for details.

%prep
%setup -q

%build

%install
################################################################################
# Backgrounds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/
for x in backgrounds/*.png backgrounds/*.jpg backgrounds/*.xml ; do
  install -p -m 644 $x $RPM_BUILD_ROOT%{_datadir}/backgrounds/
done

# Backgrounds
################################################################################

# glib 2.0 schemas
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.background.default.gschema.override \
  $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.screensaver.default.gschema.override \
  $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

# gnome background properties
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/desktop-backgrounds-default.xml \
  $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

# first boot theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
done

# pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

# m1n1 logos
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
for i in bootloader/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
done

# plymouth theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
done

# spinner theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/spinner
install -p -m 644 pixmaps/fedora-gdm-logo.png $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/spinner/watermark.png

# icons
for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_datadir}/icons/hicolor/16x16/apps/fedora-logo-icon.png favicon.png
popd

# icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/fedora-logo-icon.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/start-here.svg
install -p -m 644 icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/symbolic/apps
install -p -m 644 icons/hicolor/symbolic/apps/org.fedoraproject.AnacondaInstaller-symbolic.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/symbolic/apps/org.fedoraproject.AnacondaInstaller-symbolic.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a fedora/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}
pushd $RPM_BUILD_ROOT%{_datadir}
ln -s %{name} redhat-logos
ln -s %{name} fedora-logos
popd

# FreeIPA images
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.png $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.jpg $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images

# Test page
mkdir -p $RPM_BUILD_ROOT%{_datadir}/testpage/
cp -a testpage/index.html $RPM_BUILD_ROOT%{_datadir}/testpage/

# Some icons are duplicates, let's hardlink.
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
hardlink -v %{buildroot}/usr

# Only for x86
%ifnarch x86_64 i686
rm -f $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.lss
%endif

%post
touch --no-create %{_datadir}/icons/hicolor || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/glib-2.0/schemas/*.override
%{_datadir}/firstboot/themes/fedora-%{codename}/
%{_datadir}/plymouth/themes/charge/
%{_datadir}/plymouth/themes/spinner/

%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/anaconda/pixmaps/*
%ifarch x86_64 i686
%{_datadir}/anaconda/boot/splash.lss
%endif
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/%{name}/
%{_datadir}/redhat-logos
%{_datadir}/fedora-logos

# The below directories are multi-owned, that way we don't pull in
# excess dependencies.
%dir %{_datadir}/backgrounds
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/36x36/
%dir %{_datadir}/icons/hicolor/36x36/apps/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%dir %{_datadir}/icons/hicolor/96x96/
%dir %{_datadir}/icons/hicolor/96x96/apps/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%dir %{_datadir}/icons/hicolor/scalable/places/
%dir %{_datadir}/icons/hicolor/symbolic/
%dir %{_datadir}/icons/hicolor/symbolic/apps/
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/boot/
%dir %{_datadir}/anaconda/pixmaps
%dir %{_datadir}/firstboot/
%dir %{_datadir}/firstboot/themes/
%dir %{_datadir}/plymouth/
%dir %{_datadir}/plymouth/themes/

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png
%{_datadir}/testpage
%{_datadir}/testpage/index.html

%files ipa
%license COPYING
%{_datadir}/ipa/ui/images/*
# The below directories are multi-owned, that way we don't pull in
# excess dependencies.
%dir %{_datadir}/ipa
%dir %{_datadir}/ipa/ui
%dir %{_datadir}/ipa/ui/images

%files -n trilliumos-backgrounds
%license COPYING Attribution
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/desktop-backgrounds-default.xml

%endif

%changelog
* Tue Feb 17 2026 Shaun Assam <sassam@fedoraproject.org> - 100.4-99
- Repurposed branding and rebuilt for trilliumOS

* Tue Aug 26 2025 Louis Abel <label@resf.org> - 100.4-7
- Enable extras

* Wed May 28 2025 Louis Abel <label@resf.org> - 100.3-6
- Enable KDE backgrounds
- Use metadata.json instead

* Mon May 26 2025 Louis Abel <label@resf.org> - 100.3-3
- Add a symlink for fedora-logos

* Wed May 14 2025 Louis Abel <label@resf.org> - 100.3-2
- Add make as a BR

* Fri May 09 2025 Louis Abel <label@resf.org> - 100.3-1
- Bump logos version

* Fri Apr 18 2025 Louis Abel <label@resf.org> - 100.2-4
- Add watermark for spinner
- Add fedora-logo.ico

* Tue Nov 12 2024 Louis Abel <label@resf.org> - 100.2-2
- Rebuild to address build system issue

* Sun Sep 29 2024 Louis Abel <label@resf.org> - 100.2-1
- Install bootloader logos for m1n1

* Sat Jun 17 2023 Louis Abel <label@rockylinux.org> - 100.1-1
- Init for Rocky Linux 10 (Red Quartz)
