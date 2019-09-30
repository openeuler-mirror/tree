Name:     tree
Version:  1.7.0
Release:  17
Summary:  Tree file viewer tool
License:  GPLv2+
URL:      http://mama.indstate.edu/users/ice/tree/

Source0:  ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz

Patch0:   0000-tree-preserve-timestamps.patch
Patch1:   0001-tree-args.patch
Patch2:   0002-tree-dircolors-ec.patch
Patch3:   0003-tree-size-field-len.patch

BuildRequires: gcc git

%description
Tree is a recursive directory listing command that produces a depth indented
listing of files, which is colorized ala dircolors if the LS_COLORS environment
variable is set and output is to tty.


%package        help
Summary:        Including man files for tree
Requires:       man

%description    help
This contains man files for the using of tree.

%prep
%autosetup -n %{name}-%{version} -p1 -S git

#fix non-ASCII characters abnormal display
sed -e 's/LINUX/__linux__/' -i tree.c

%build
%make_build CFLAGS="$RPM_OPT_FLAGS $(getconf LFS_CFLAGS)" LDFLAGS="$RPM_LD_FLAGS"

%install
install -D -m 755 tree $RPM_BUILD_ROOT%{_bindir}/tree
install -D -m 644 doc/tree.1 $RPM_BUILD_ROOT%{_mandir}/man1/tree.1

%files
%license LICENSE
%doc README CHANGES
%{_bindir}/tree

%files help
%{_mandir}/man1/*

%changelog
* Wed Aug 21 2019 zhanghaibo <ted.zhang@huawei.com>  - 1.7.0-17
- Type:enhancemnet
- ID:NA
- SUG:NA
- DESCi:openEuler Debranding

* Tue Aug 20 2019 huangzheng <huangzheng22@huawei.com> - 1.7.0-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:rename patches
- Package init
