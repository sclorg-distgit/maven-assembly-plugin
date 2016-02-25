%global pkg_name maven-assembly-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.4
Release:        8.12%{?dist}
Summary:        Maven Assembly Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-assembly-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:file-management)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-repository-builder)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-io)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)


%description
A Maven plugin to create archives of your project's sources, classes,
dependencies etc. from flexible assembly descriptors.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
# Tests need easymockclassextension version 2.x, which is incompatible
# with easymockclassextension version 3.x we have in Fedora.
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 2.4-8.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.4-8.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.4-8.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.8
- Fix BR on maven-plugins parent POM

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.4-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.4-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.4-8
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-6
- Build with xmvn
- Install license files
- Resolves: rhbz#915608

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 13 2012 Tomas Radej <tradej@redhat.com> - 2.4-1
- Updated to latest upstream version.
- Fixed mail in changelog

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 2.3-3
- Migration to plexus-containers-container-default

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Tomas Radej <tradej@redhat.com> - 2.3-1
- Update to latest upstream vresion.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Tomas Radej <tradej@redhat.com> - 2.2.2-3
- Added R on plexus-containers-component-metadata

* Mon Dec 12 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-2
- Remove plexus-maven-plugin require.

* Tue Dec 6 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.2-1
- Update to latest upstream version.

* Sun Oct 2 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-4
- Add missing BR/R.

* Thu Jul 15 2011 Jaromir Capik <jcapik@redhat.com> 2.2.1-3
- modello removed from requires
- %update_maven_depmap removed

* Thu May 23 2011 Jaromir Capik <jcapik@redhat.com> 2.2.1-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Missing modello dependency added
- Minor spec file changes according to the latest guidelines

* Thu Mar 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-1
- Update to upstream 2.2.1 release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2-1
- Update to final release.

* Tue Jun 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2-0.4.beta5
- Add missing BuildRequires.

* Tue Jun 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2-0.3.beta5
- Add missing Requires.

* Thu Jun 03 2010 Yong Yang <yyang@redhat.com> - 2.2-0.2.beta5
- Chmod 0644 for depmap.xml
- Fix Obsoletes and Provides
- Change to BR java

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 2.2-0.1.beta5
- Initial build
