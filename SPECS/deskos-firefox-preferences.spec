Name:           deskos-firefox-preferences
Version:        0.2.0
Release:        2%{?dist}
Summary:        Configure Firefox preferences for DeskOS

Group:          Applications/Internet
License:        GPLv3+
URL:            https://deskosproject.org
Source0:        all-deskos.js
Source1:        deskos-firefox-theme-default-prefs.js

Requires:       firefox

%description
Configure Firefox preferences for DeskOS.

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/firefox/defaults/preferences/
cp -a %{SOURCE0} $RPM_BUILD_ROOT/%{_libdir}/firefox/defaults/preferences/
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_libdir}/firefox/defaults/preferences/

%files
%defattr(-,root,root,-)
%{_libdir}/firefox/defaults/preferences/all-deskos.js
%{_libdir}/firefox/defaults/preferences/deskos-firefox-theme-default-prefs.js

%changelog
* Thu Dec 22 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2.0-2
- Removed BuildArch: noarch

* Tue Dec 20 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2.0-1
- Set DeskOS Firefox Theme as default

* Sun Sep 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial release
