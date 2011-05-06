%define name	xwpick
%define	version	2.20

Name:		%{name}
Summary:	A X Window System screenshot grabber
Version:	%{version}
Release:	%mkrel 19
License:	MIT
Group:		Graphics
BuildRequires:	imake libx11-devel libxext-devel
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.bz2
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The xwpick program allows you to choose an image or a rectangular piece
of an image from an X Window System window and then write the image to
a file in a variety of formats, incuding PostScript(TM), GIF, and PICT.

%prep
%setup -q

%build
xmkmf
perl -pi -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -pi -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile 
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std} install.man

# icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

# Menu entry

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xwpick
Comment=Screenshot grabber
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;2DGraphics;
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/xwpick.1*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
