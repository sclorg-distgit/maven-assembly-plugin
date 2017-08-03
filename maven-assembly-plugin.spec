%{?scl:%scl_package maven-assembly-plugin}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}maven-assembly-plugin
Version:        3.0.0
Release:        2.2%{?dist}
Summary:        Maven Assembly Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-assembly-plugin/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(com.google.code.findbugs:jsr305)
BuildRequires:  %{?scl_prefix}mvn(commons-codec:commons-codec)
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-artifact)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-model)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:file-management)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-io)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
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
%setup -n %{pkg_name}-%{version} -q

%build
# Tests need easymockclassextension version 2.x, which is incompatible
# with easymockclassextension version 3.x we have in Fedora.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 3.0.0-2.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0.0-2.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Thu Jun 30 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8
- Compile against Maven 3 APIs

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-7
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-5
- Port to Maven Shared IO 3.0.0

* Wed Dec  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-4
- Rebuild for maven-common-artifact-filters ABI change

* Tue Nov 10 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-3
- Port to maven-filtering 3.0.0

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-2
- Rebuild for maven-common-artifact-filters 3.0 ABI

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Thu Jul 02 2015 Michael Simacek <msimacek@redhat.com> - 2.5.5-3
- Port to current plexus-archiver

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.5-1
- Update to upstream version 2.5.5

* Mon Apr 27 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.4-1
- Update to upstream version 2.5.4

* Thu Mar 26 2015 Michael Simacek <msimacek@redhat.com> - 2.5.3-1
- Update to upstream version 2.5.3

* Fri Feb 13 2015 gil cattaneo <puntogil@libero.it> - 2.5.2-2
- introduce license macro

* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-1
- Update to upstream version 2.5.2

* Thu Nov  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-3
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-2
- Update to plexus-archiver 2.6.1 and plexus-io 2.1.1

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.1-1
- Update to upstream version 2.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-9
- Add missing BR on modello
- Resolves: rhbz#1077910

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-8
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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

* Mon Jul 15 2011 Jaromir Capik <jcapik@redhat.com> 2.2.1-3
- modello removed from requires
- %update_maven_depmap removed

* Mon May 23 2011 Jaromir Capik <jcapik@redhat.com> 2.2.1-2
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
