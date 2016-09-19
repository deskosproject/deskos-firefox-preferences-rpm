Name:           deskos-firefox-preferences
Version:        0.1.0
Release:        1%{?dist}
Summary:        Configure Firefox preferences for DeskOS

Group:          Applications/Internet 
License:        GPLv3+
URL:            https://deskosproject.org
Source0:        all-deskos.js

Requires:       firefox

%description
Configure Firefox preferences for DeskOS.

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/firefox/defaults/preferences
cp -a %SOURCE0 $RPM_BUILD_ROOT/%{_libdir}/firefox/defaults/preferences

%files
%defattr(-,root,root,-)
%{_libdir}/firefox/defaults/preferences/all-deskos.js

%changelog
* Sun Sep 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial release