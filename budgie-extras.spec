Name:		budgie-extras
Version:	1.2.0
Release:	1%{dist}
License:	GPLv3
Summary:	Additional Budgie Desktop enhancements for user experience
URL:		https://ubuntubudgie.org/

Source0:	https://github.com/UbuntuBudgie/budgie-extras/releases/download/v%{version}/budgie-extras-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	vala
BuildRequires:	intltool

BuildRequires:	pkgconfig(budgie-1.0)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(keybinder-3.0)
BuildRequires:	pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(libnma)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libwnck-3.0)

%if 0%{?fedora}
BuildRequires:	pkgconfig(appstream)
BuildRequires:	pkgconfig(granite)
BuildRequires:	pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(zeitgeist-2.0)

Requires:	budgie-applet-applications-menu
Requires:	budgie-applet-weathershow
%endif

Requires:	budgie-applet-app-launcher
Requires:	budgie-applet-brightness-controller
Requires:	budgie-applet-clockworks
Requires:	budgie-applet-countdown
Requires:	budgie-applet-dropby
Requires:	budgie-applet-fuzzyclock
Requires:	budgie-applet-hotcorners
Requires:	budgie-applet-kangaroo
Requires:	budgie-applet-keyboard-autoswitch
Requires:	budgie-applet-network-manager
Requires:	budgie-applet-quickchar
Requires:	budgie-applet-quicknote
Requires:	budgie-applet-recentlyused
Requires:	budgie-applet-rotation-lock
Requires:	budgie-applet-showtime
Requires:	budgie-applet-takeabreak
Requires:	budgie-applet-trash
Requires:	budgie-applet-visualspace
Requires:	budgie-applet-wallstreet
Requires:	budgie-applet-window-shuffler
Requires:	budgie-applet-wmover
Requires:	budgie-applet-workspace-stopwatch
Requires:	budgie-applet-wpreviews
Requires:	budgie-applet-wsoverview
Requires:	budgie-applet-wswitcher

%description
This is part of a suite of python3 and Vala based applets for the Budgie
Desktop that provide additional user orientated capabilities.
The applets can be used individually or as a set.

%package	common
Requires:	budgie-desktop
Summary:	Shared component of budgie-extras applets
%description	common
The shared component provides for capabilities that are utilised between
budgie-extra applets.

%package	daemon
Summary:	Manages keyboard shortcuts
Requires:	budgie-extras-common
%description	daemon
This on logon process manages keyboard shortcuts delivered via .bde files for
various extras-plugins.

%package -n	budgie-applet-app-launcher
Requires:	budgie-extras-common
Summary:	Applet to provide an alternative means to launch applications
%description -n	budgie-applet-app-launcher
The app-launcher applet allows the ability to add favorite apps to the
panel as well as finding and launching applications.  The list of
applications listed can be easily configured to be visible or hidden.

%if 0%{?fedora}
%package -n	budgie-applet-applications-menu
Requires:	budgie-extras-common
Summary:	Lightweight and stylish app launcher
%description -n	budgie-applet-applications-menu
%{summary}
%endif

%package -n	budgie-applet-brightness-controller
Requires:	budgie-extras-common
Summary:	A Budgie Desktop applet for productivity
%description -n	budgie-applet-brightness-controller
%{summary}

%package -n	budgie-applet-clockworks
Requires:	budgie-extras-common
Summary:	Applet to display clock across multiple time zones
%description -n	budgie-applet-clockworks
The Clockworks applet displays the current time across multiple
time zones.

%package -n	budgie-applet-countdown
Requires:	budgie-extras-common
Summary:	Applet providing a countdown capability on the Budgie Desktop
%description -n	budgie-applet-countdown
The Countdown applet provides the user the ability to start an
action when the countdown reaches 0 seconds. Actions include flashing
an icon in the panel, opening a notification window, sounding a
bell or running a custom command.

%package -n	budgie-applet-dropby
Requires:	budgie-extras-common
Summary:	Applet to popup when a USB device is connected
%description -n	budgie-applet-dropby
The DropBy applet pops up in the panel when connecting a usb device.
The applet subsequently offers the option(s) to mount, unmount/eject
and in case of a flash drive, to make a local copy of the drive's
content. The info shows the free space on the volume.

%package -n	budgie-applet-fuzzyclock
Requires:	budgie-extras-common
Summary:	Shows the time in a Fuzzy Way
%description -n	budgie-applet-fuzzyclock
%{summary}

%package -n	budgie-applet-hotcorners
Requires:	budgie-extras-common
Summary:	Applet providing hotcorners capabilities for the Budgie Desktop
%description -n	budgie-applet-hotcorners
The hotcorners applet allow user defined commands to be executed
when the mouse cursor is pushed into a corner of the main desktop.

%package -n	budgie-applet-kangaroo
Requires:	budgie-extras-common
Summary:	Applet to allow quick file-browsing
%description -n	budgie-applet-kangaroo
The kangaroo applet allows for quick & easy browsing, across
(possibly) many directory layers, without having to do a single mouse
click.

%package -n	budgie-applet-keyboard-autoswitch
Requires:	budgie-extras-common
Summary:	Applet adding the ability to set a different keyboard layout per application
%description -n	budgie-applet-keyboard-autoswitch
The Keyboard Auto Switcher applet provides the user the ability to set
a different keyboard layout per application. Exceptions to the default
layout can be set by simply choosing a different layout using the
Keyboard Layout applet.

%package -n	budgie-applet-network-manager
Requires:	budgie-extras-common
Summary:	A fork of Wingpanel Network Indicator, ported to budgie desktop
%description -n	budgie-applet-network-manager
%{summary}

%package -n	budgie-applet-quickchar
Requires:	budgie-extras-common
Summary:	A mini-app to quickly choose and insert equivalents of ascii characters
%description -n	budgie-applet-quickchar
QuickChar is a mini-app to quickly choose and insert equivalents of ascii
characters. QuickChar is activated via the Budgie Menu.

%package -n	budgie-applet-quicknote
Requires:	budgie-extras-common
Summary:	Applet providing simple notes capability for the Budgie Desktop
%description -n	budgie-applet-quicknote
The quicknote applet allows a user to record a text based note.
The applet supports multiple undo and redo capabilities.

%package -n	budgie-applet-recentlyused
Requires:	budgie-extras-common
Summary:	Applet displays files recently accessed for the Budgie Desktop
%description -n	budgie-applet-recentlyused
The recentlyused applet displays the users files that have been opened
or created within a configurable period of time.

%package -n	budgie-applet-rotation-lock
Requires:	budgie-extras-common
Summary:	Applet to lock or unlock the screen rotation
%description -n	budgie-applet-rotation-lock
The Rotation Lock applet provides the user an easy way to lock or
unlock the screen rotation.

%package -n	budgie-applet-showtime
Requires:	budgie-extras-common
Summary:	Applet displaying date and time on the Budgie Desktop
%description -n	budgie-applet-showtime
The ShowTime applet is a digital desktop clock, showing time and/or
date.  Text color of both the displayed time and date can be set
separately from the applet's menu

%package -n	budgie-applet-takeabreak
Requires:	budgie-extras-common
Summary:	A pomodoro-like applet, to make sure to take regular breaks from working
%description -n	budgie-applet-takeabreak
Budgie TakeaBreak is a pomodoro- like applet, to make sure to take regular
breaks from working. Options from Budgie Settings include turning the screen
upside down, dim the screen, lock screen or show a countdown message on break
time. The applet can be accessed quickly from the panel to temporarily switch
it off.

%package -n	budgie-applet-trash
Requires:	budgie-extras-common
Summary:	Applet allows access to trash capabilities for the Budgie Desktop
%description -n	budgie-applet-trash
The trash applet allows the user access the desktop trash capabilities
from the panel including the ability to delete and restore files stored
in the trash folder.

%package -n	budgie-applet-visualspace
Requires:	budgie-extras-common
Summary:	Shows the current workspace(s), as bullet(s)
%description -n	budgie-applet-visualspace
Budgie VisualSpace shows the current workspace(s), as bullet(s). The applet
includes a menu to navigate to either one of the windows or their
corresponding workspace.

%package -n	budgie-applet-wallstreet
Requires:	budgie-extras-common
Summary:	A mini-app to switch wallpapers on regular intervalls
%description -n	budgie-applet-wallstreet
Budgie WallStreet is a mini-app to switch wallpapers on regular intervalls.

%if 0%{?fedora}
%package -n	budgie-applet-weathershow
Requires:	budgie-extras-common
Summary:	Applet to display the weather and forecast
%description -n	budgie-applet-weathershow
The weathershow applet displays daily and three hourly weather
forecasts on both the desktop and a Popover.
%endif

%package -n	budgie-applet-window-shuffler
Requires:	budgie-extras-common
Summary:	Budgie Window Shuffler
%description -n	budgie-applet-window-shuffler
%{summary}

%package -n	budgie-applet-wmover
Requires:	budgie-extras-common
Summary:	An applet to quickly move windows to any of the other workspaces
%description -n	budgie-applet-wmover
Budgie WindoMover is an application (applet) to quickly move windows to any of
the other workspaces. Just drag a window to the bottom of the screen and a bar
will popup, representing the workspaces. Click on any of the numbers (or press
the corresponding number on the keyboard), and the window will move to that
workspace

%package -n	budgie-applet-workspace-stopwatch
Requires:	budgie-extras-common
Summary:	An applet to keep track of usage per workspace
%description -n	budgie-applet-workspace-stopwatch
Workspace Timer Applet is an applet to keep track of usage per workspace, e.g.
to find out how much minutes/hours were actually spent on a job. Workspaces can
be freely named, custom names and all data are rmembered, also after
logout/restart, until the RESET button is pressed. The log file is updated
onworkspace switch/clicking the icon for popup or else every 30 seconds. Time
during suspend is automatically retracted from a workspace' time.

%package -n	budgie-applet-wpreviews
Requires:	budgie-extras-common
Summary:	Applet providing window previews capabilities for the Budgie Desktop
%description -n	budgie-applet-wpreviews
The Previews applet shows an overview of windows in an expose like way.

%package -n	budgie-applet-wsoverview
Requires:	budgie-extras-common
Summary:	Applet providing quick access to workspaces for the Budgie Desktop
%description -n	budgie-applet-wsoverview
The workspace overview applet allows a user to quickly navigate
workspaces using the applet's menu.  Optionally, navigation to any
window in any workspace is possible.

%package -n	budgie-applet-wswitcher
Requires:	budgie-extras-common
Summary:	An applet to show a different wallpaper on each of the workspaces
%description -n	budgie-applet-wswitcher
Budgie Wallpaper Workspace Switcher is an application (applet) to show a
different wallpaper on each of the workspaces. Usage is simple: add the applet
to the panel and set wallpapers on each of the workspaces in the way you are
used to. The applet will remember what wallpaper was set on each of the
workspaces.

%prep
%autosetup

%build
%if 0%{?fedora}
%meson
%else
%meson \
	-Dbuild-all=true \
	-Dbuild-wpreviews=true \
	-Dbuild-wswitcher=true \
	-Dbuild-hotcorners=true \
	-Dbuild-quicknote=true \
	-Dbuild-wmover=true \
	-Dbuild-wsoverview=true \
	-Dbuild-showtime=true \
	-Dbuild-countdown=true \
	-Dbuild-keyboard-autoswitch=true \
	-Dbuild-rotation-lock=true \
	-Dbuild-clockworks=true \
	-Dbuild-dropby=true \
	-Dbuild-kangaroo=true \
	-Dbuild-trash=true \
	-Dbuild-app-launcher=true \
	-Dbuild-recentlyused=true \
	-Dbuild-takeabreak=true \
	-Dbuild-workspacestopwatch=true \
	-Dbuild-extrasdaemon=true \
	-Dbuild-quickchar=true \
	-Dbuild-fuzzyclock=true \
	-Dbuild-brightness-controller=true \
	-Dbuild-visualspace=true \
	-Dbuild-wallstreet=true \
	-Dbuild-network-manager=true \
	-Dbuild-window-shuffler=true
%endif

%meson_build

%install
%meson_install

%files

%files common
%{_datadir}/locale

%files daemon
%{_sysconfdir}/xdg/autostart/budgie-extras-daemon.desktop
%{_bindir}/budgie-extras-daemon
%{_libdir}/budgie-extras-daemon/invoke.py
%{_datadir}/budgie-desktop/layouts/*.layout
%{_datadir}/budgie-extras-daemon
%{_mandir}/man1/budgie-extras-daemon.1.gz

%files -n budgie-applet-app-launcher
%{_datadir}/pixmaps/budgie-app-launcher*.svg
%{_libdir}/budgie-desktop/plugins/budgie-app-launcher

%if 0%{?fedora}
%files -n budgie-applet-applications-menu
%{_libdir}/budgie-desktop/plugins/applications-menu
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-appmenu.gschema.xml
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%endif

%files -n budgie-applet-brightness-controller
%{_libdir}/budgie-desktop/plugins/budgie-brightness-controller
%{_datadir}/pixmaps/budgie-brightness-controller-1-symbolic.svg

%files -n budgie-applet-clockworks
%{_libdir}/budgie-desktop/plugins/budgie-clockworks
%{_datadir}/glib-2.0/schemas/*budgie-clockworks*.xml
%{_datadir}/pixmaps/budgie-clockworks*.svg

%files -n budgie-applet-countdown
%{_libdir}/budgie-desktop/plugins/budgie-countdown
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-countdown.gschema.xml
%{_datadir}/pixmaps/budgie-countdown-symbolic.svg
%{_datadir}/pixmaps/cr_*.png

%files -n budgie-applet-dropby
%{_libdir}/budgie-desktop/plugins/budgie-dropby
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-dropby.gschema.xml
%{_datadir}/pixmaps/budgie-dropby*.svg

%files -n budgie-applet-fuzzyclock
%{_libdir}/budgie-desktop/plugins/budgie-fuzzyclock

%files -n budgie-applet-hotcorners
%{_libdir}/budgie-desktop/plugins/budgie-hotcorners
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-hotcorners.gschema.xml
%{_datadir}/pixmaps/budgie-hotcorners-symbolic.svg

%files -n budgie-applet-kangaroo
%{_libdir}/budgie-desktop/plugins/budgie-kangaroo
%{_datadir}/pixmaps/budgie-foldertrack-symbolic.svg

%files -n budgie-applet-keyboard-autoswitch
%{_libdir}/budgie-desktop/plugins/budgie-keyboard-autoswitch
%{_datadir}/pixmaps/budgie-keyboard-autoswitch-symbolic.svg

%files -n budgie-applet-network-manager
%{_libdir}/budgie-desktop/plugins/budgie-network-manager

%files -n budgie-applet-quickchar
%{_sysconfdir}/xdg/autostart/quickchar-autostart.desktop
%{_bindir}/quickchar
%{_libdir}/quickchar
%{_datadir}/applications/quickchar.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.quickchar.gschema.xml
%{_datadir}/quickchar/chardata
%{_mandir}/man1/quickchar.1.gz

%files -n budgie-applet-quicknote
%{_libdir}/budgie-desktop/plugins/budgie-quicknote
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.quicknote.gschema.xml
%{_datadir}/pixmaps/budgie-quicknote-symbolic.svg

%files -n budgie-applet-recentlyused
%{_libdir}/budgie-desktop/plugins/budgie-recentlyused
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-recentlyused.gschema.xml

%files -n budgie-applet-rotation-lock
%{_libdir}/budgie-desktop/plugins/budgie-rotation-lock
%{_datadir}/pixmaps/budgie-rotation-*.svg

%files -n budgie-applet-showtime
%{_libdir}/budgie-desktop/plugins/budgie-showtime
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-showtime.gschema.xml
%{_datadir}/pixmaps/showtimenew-symbolic.svg

%files -n budgie-applet-takeabreak
%{_libdir}/budgie-desktop/plugins/budgie-takeabreak
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.takeabreak.gschema.xml
%{_datadir}/pixmaps/takeabreak*.svg

%files -n budgie-applet-trash
%{_libdir}/budgie-desktop/plugins/budgie-trash
%{_datadir}/pixmaps/budgie-trash-*.svg

%files -n budgie-applet-visualspace
%{_sysconfdir}/xdg/autostart/visualspace-autostart.desktop
%{_libdir}/budgie-desktop/plugins/budgie-visualspace
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-visualspace.gschema.xml
%{_datadir}/pixmaps/visualspace-symbolic.svg

%files -n budgie-applet-wallstreet
%{_sysconfdir}/xdg/autostart/wallstreet-autostart.desktop
%{_libdir}/budgie-wallstreet/wallstreet*
%{_datadir}/applications/wallstreet-control.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-wallstreet.gschema.xml
%{_datadir}/pixmaps/wallstreet-control.svg

%if 0%{?fedora}
%files -n budgie-applet-weathershow
%{_libdir}/budgie-desktop/plugins/budgie-weathershow
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.weathershow.gschema.xml
%{_datadir}/pixmaps/budgie-wticon-symbolic.svg
%endif

%files -n budgie-applet-window-shuffler
%{_sysconfdir}/xdg/autostart/layoutspopup-autostart.desktop
%{_sysconfdir}/xdg/autostart/shuffler*.desktop
%{_libdir}/budgie-window-shuffler
%{_datadir}/applications/shuffler-control.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.windowshuffler.gschema.xml
%{_datadir}/pixmaps/shuffler-*.svg

%files -n budgie-applet-wmover
%{_libdir}/budgie-desktop/plugins/budgie-wmover
%{_datadir}/pixmaps/budgie-wmover-symbolic.svg

%files -n budgie-applet-workspace-stopwatch
%{_libdir}/budgie-desktop/plugins/budgie-workspace-stopwatch
%{_datadir}/pixmaps/budgie-wstopwatch-symbolic.svg

%files -n budgie-applet-wpreviews
%{_sysconfdir}/xdg/autostart/previews-*.desktop
%{_libdir}/budgie-previews
%{_datadir}/applications/previewscontrols.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-wpreviews.gschema.xml
%{_datadir}/pixmaps/budgie_wpreviews_*.png
%{_datadir}/pixmaps/budgiewprviews.svg

%files -n budgie-applet-wsoverview
%{_libdir}/budgie-desktop/plugins/budgie-wsoverview
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-wsoverview.gschema.xml
%{_datadir}/pixmaps/budgie-wsoverview-symbolic.svg
%{_datadir}/pixmaps/ws*-symbolic.svg

%files -n budgie-applet-wswitcher
%{_libdir}/budgie-desktop/plugins/budgie-wswitcher
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-wswitcher.gschema.xml
%{_datadir}/pixmaps/budgie-wsw-symbolic.svg

%changelog
* Fri Apr 16 2021 Thomas Batten <stenstorpmc@gmail.com> - 1.2.0-1
- Initial Build
