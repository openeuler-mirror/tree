Name:     tree
Version:  2.1.0
Release:  2
Summary:  Tree file viewer tool
License:  GPLv2+
URL:      http://mama.indstate.edu/users/ice/tree/

Source0:  http://mama.indstate.edu/users/ice/tree/src/%{name}-%{version}.tgz
Source1:  ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz
Patch0:   0001-Support-specify-CC.patch

BuildRequires: gcc

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
%autosetup -n %{name}-%{version} -p1

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
* Wed Apr 19 2023 jammyjellyfish <jammyjellyfish255@outlook.com> - 2.1.0-2
- Support specify CC

* Thu Feb 09 2023 Kunlin Yang <yangkunlin7@huawei.com> - 2.1.0-1
- upgrade package from 2.0.4 to 2.1.0

* Wed Nov 16 2022 Kunlin Yang <yangkunlin7@huawei.com> - 2.0.4-2
- add SOURCE http url

* Fri Oct 28 2022 Kunlin Yang <yangkunlin7@huawei.com> - 2.0.4-1
- upgrade package from 1.8.0 to 2.0.4

* Tue Jul 12 2022 xueyamao <xueyamao@kylinos.cn> - 1.8.0-3
- DESC: Document --du and --prune options in help output

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 1.8.0-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Thu Jul 16 2020 zhangyouming <zhangyouming4@huawei.com> - 1.8.0-1
upgrade package from 1.7.0 to 1.8.0

* Wed Jan 8 2020 openEuler BuildTeam <buildteam@openeuler.org> - 1.7.0-18
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Repackage

* Wed Aug 21 2019 zhanghaibo <ted.zhang@huawei.com>  - 1.7.0-17
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:openEuler Debranding

* Tue Aug 20 2019 huangzheng <huangzheng22@huawei.com> - 1.7.0-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:rename patches
- Package init
