Name:		xwpick
Summary:	A X Window System screenshot grabber
Version:	2.20
Release:	32
License:	MIT
Group:		Graphics
BuildRequires:	imake 
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.bz2
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png

%description
The xwpick program allows you to choose an image or a rectangular piece
of an image from an X Window System window and then write the image to
a file in a variety of formats, incuding PostScript(TM), GIF, and PICT.

%prep
%setup -q

%build
xmkmf
perl -pi -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = %{optflags}|" Makefile
perl -pi -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = %{optflags}|" Makefile 
%make

%install
%{makeinstall_std} install.man

# icons
install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

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

%files
%{_bindir}/%{name}
%{_mandir}/man1/xwpick.1*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.20-19mdv2011.0
+ Revision: 671378
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.20-18mdv2011.0
+ Revision: 608246
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.20-17mdv2010.1
+ Revision: 524475
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.20-16mdv2009.1
+ Revision: 350737
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.20-15mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.20-15mdv2008.1
+ Revision: 179440
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Jun 18 2007 Adam Williamson <awilliamson@mandriva.org> 2.20-14mdv2008.0
+ Revision: 40754
- new X layout; trim buildrequires; XDG menu; fd.o icons; rebuild for new era


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.20-13mdk
- Rebuild

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.20-12mdk
- fix buildrequires
- cleanups!

* Sun May 04 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.20-11mdk
- rebuild for rpm 4.2
- png icons

* Mon Aug 20 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 2.20-10mdk
- fixed typo in menu

* Sat Aug 11 2001 Jesse Kuang <kjx@mandrakesoft.com> 2.20-9mdk
- rebuilt for cooker

* Tue Aug 29 2000 David BAUDENS <baudens@mandrakesoft.com> 2.20-8mdk
- Fix crazy menu entry
- Fix crazy Group
- Fix crazy macros

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.20-7mdk
- automatically added BuildRequires

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.20-6mdk
- use new macros
- don't strip : let spechelper do it

* Mon May 15 2000 David BAUDENS <baudens@mandrakesoft.com> 2.20-5mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot

* Fri Apr 07 2000 Denis Havlik <denis@mandrakesoft.com> 2.20-4mdk
- group: toys
- menu entry + icons (need beter icons)

* Fri Nov 05 1999 Damien Krotkine <damien@mandrakesoft.com> 2.20-3mdk
- Mandrake release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 11)

* Sun Dec 20 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

