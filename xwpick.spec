%define name	xwpick
%define	version	2.20
%define	release	13mdk

Name:		%{name}
Summary:	A X Window System screenshot grabber

Version:	%{version}
Release:	%{release}
License:	MIT
Icon:		%{name}.xpm
Group:		Graphics
BuildRequires:	XFree86-devel X11
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
perl -p -i -e "s|CXXDEBUGFLAGS = .*|CXXDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile
perl -p -i -e "s|CDEBUGFLAGS = .*|CDEBUGFLAGS = $RPM_OPT_FLAGS|" Makefile 
%make

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std} install.man

# icons
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

# Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(xwpick):\
	command="%{_prefix}/X11R6/bin/xwpick"\
	needs="text"\
	icon="xwpick.png"\
	section="Multimedia/Graphics"\
	title="Xwpick"\
	longtitle="X Window System screenshot grabber"
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%{_prefix}/X11R6/bin/xwpick
%{_prefix}/X11R6/man/man1/xwpick.1*
%{_prefix}/X11R6/lib/X11/doc/html/xwpick.1.html
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

