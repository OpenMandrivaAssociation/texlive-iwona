# revision 19611
# category Package
# catalog-ctan /fonts/iwona
# catalog-date 2010-08-03 20:49:06 +0200
# catalog-license gfsl
# catalog-version 0.995b
Name:		texlive-iwona
Version:	0.995b
Release:	6
Summary:	A two-element sans-serif font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/iwona
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwona.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iwona.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Iwona is a two-element sans-serif typeface. It was created as
an alternative version of the Kurier typeface, which was
designed in 1975 for a diploma in typeface design at the Warsaw
Academy of Fine Arts under the supervision of Roman
Tomaszewski. This distribution contains a significantly
extended set of characters covering the following modern
alphabets: latin (including Vietnamese), Cyrillic and Greek as
well as a number of additional symbols (including mathematical
symbols). The fonts are prepared in Type 1 and OpenType
formats. For use with TeX the following encoding files have
been prepared: T1 (ec), T2 (abc), and OT2--Cyrillic, T5
(Vietnamese), OT4, QX, texansi and nonstandard (IL2 for the
Czech fonts), as well as supporting macros and files defining
fonts for LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonab.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonabi.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacb.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacbi.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonach.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonachi.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacl.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacli.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacm.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacmi.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacr.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonacri.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonah.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonahi.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonal.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonali.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonam.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonami.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonar.afm
%{_texmfdistdir}/fonts/afm/nowacki/iwona/iwonari.afm
%{_texmfdistdir}/fonts/enc/dvips/iwona/cs-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/cs-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/ec-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/ec-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/ex-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/greek-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/l7x-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/l7x-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/mi-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/qx-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/qx-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/rm-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/rm-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/sy-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/t2a-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/t2b-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/t2c-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/t5-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/t5-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/texnansi-iwona-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/texnansi-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/ts1-iwona.enc
%{_texmfdistdir}/fonts/enc/dvips/iwona/wncy-iwona.enc
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-cs.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-ec.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-ex.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-greek.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-l7x.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-mi.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-qx.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-rm.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-sy.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-t2a.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-t2b.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-t2c.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-t5.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-ts1.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona-wncy.map
%{_texmfdistdir}/fonts/map/dvips/iwona/iwona.map
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/Iwona-Bold.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/Iwona-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/Iwona-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/Iwona-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCond-Bold.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCond-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCond-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCond-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondHeavy-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondHeavy-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondMedium-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaCondMedium-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaHeavy-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaHeavy-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaMedium-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/iwona/IwonaMedium-Regular.otf
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/cs-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ec-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ex-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/greek-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/l7x-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/mi-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/qx-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/rm-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonabz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonacbz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonachz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonaclz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonacmz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonacrz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonahz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonalz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonamz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/sy-iwonarz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2a-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2b-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t2c-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/t5-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonab-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonabi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonach-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonachi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonah-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonahi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonal-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonali-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonam-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonami-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonar-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonari-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/texnansi-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/ts1-iwonari.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonab.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonabi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonach.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonachi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonacri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonah.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonahi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonal.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonali.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonam.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonami.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonar.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/iwona/wncy-iwonari.tfm
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonab.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonabi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacb.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacbi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonach.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonachi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacl.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacli.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacm.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacmi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacr.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonacri.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonah.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonahi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonal.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonali.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonam.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonami.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonar.pfb
%{_texmfdistdir}/fonts/type1/nowacki/iwona/iwonari.pfb
%{_texmfdistdir}/tex/latex/iwona/il2iwona.fd
%{_texmfdistdir}/tex/latex/iwona/il2iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/il2iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/il2iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/iwona.sty
%{_texmfdistdir}/tex/latex/iwona/l7xiwona.fd
%{_texmfdistdir}/tex/latex/iwona/l7xiwonac.fd
%{_texmfdistdir}/tex/latex/iwona/l7xiwonal.fd
%{_texmfdistdir}/tex/latex/iwona/l7xiwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/ly1iwona.fd
%{_texmfdistdir}/tex/latex/iwona/ly1iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/ly1iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/ly1iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/omliwona.fd
%{_texmfdistdir}/tex/latex/iwona/omliwonac.fd
%{_texmfdistdir}/tex/latex/iwona/omliwonal.fd
%{_texmfdistdir}/tex/latex/iwona/omliwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/omsiwona.fd
%{_texmfdistdir}/tex/latex/iwona/omsiwonac.fd
%{_texmfdistdir}/tex/latex/iwona/omsiwonal.fd
%{_texmfdistdir}/tex/latex/iwona/omsiwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/omxiwona.fd
%{_texmfdistdir}/tex/latex/iwona/omxiwonac.fd
%{_texmfdistdir}/tex/latex/iwona/omxiwonal.fd
%{_texmfdistdir}/tex/latex/iwona/omxiwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwona.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonacm.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonalcm.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonalm.fd
%{_texmfdistdir}/tex/latex/iwona/ot1iwonam.fd
%{_texmfdistdir}/tex/latex/iwona/ot2iwona.fd
%{_texmfdistdir}/tex/latex/iwona/ot2iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/ot2iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/ot2iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/ot4iwona.fd
%{_texmfdistdir}/tex/latex/iwona/ot4iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/ot4iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/ot4iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/qxiwona.fd
%{_texmfdistdir}/tex/latex/iwona/qxiwonac.fd
%{_texmfdistdir}/tex/latex/iwona/qxiwonal.fd
%{_texmfdistdir}/tex/latex/iwona/qxiwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/t1iwona.fd
%{_texmfdistdir}/tex/latex/iwona/t1iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/t1iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/t1iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/t2aiwona.fd
%{_texmfdistdir}/tex/latex/iwona/t2aiwonac.fd
%{_texmfdistdir}/tex/latex/iwona/t2aiwonal.fd
%{_texmfdistdir}/tex/latex/iwona/t2aiwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/t2biwona.fd
%{_texmfdistdir}/tex/latex/iwona/t2biwonac.fd
%{_texmfdistdir}/tex/latex/iwona/t2biwonal.fd
%{_texmfdistdir}/tex/latex/iwona/t2biwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/t2ciwona.fd
%{_texmfdistdir}/tex/latex/iwona/t2ciwonac.fd
%{_texmfdistdir}/tex/latex/iwona/t2ciwonal.fd
%{_texmfdistdir}/tex/latex/iwona/t2ciwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/t5iwona.fd
%{_texmfdistdir}/tex/latex/iwona/t5iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/t5iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/t5iwonalc.fd
%{_texmfdistdir}/tex/latex/iwona/ts1iwona.fd
%{_texmfdistdir}/tex/latex/iwona/ts1iwonac.fd
%{_texmfdistdir}/tex/latex/iwona/ts1iwonal.fd
%{_texmfdistdir}/tex/latex/iwona/ts1iwonalc.fd
%{_texmfdistdir}/tex/plain/iwona/iwona-math.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/00readme.eng
%doc %{_texmfdistdir}/doc/fonts/iwona/00readme.pol
%doc %{_texmfdistdir}/doc/fonts/iwona/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-info-src.zip
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-info.pdf
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-latex-cyr.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-latex-math.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-latex-pl.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-latex-t2a.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-latex-t5.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-mathtest.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/iwona-table.tex
%doc %{_texmfdistdir}/doc/fonts/iwona/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.995b-2
+ Revision: 752890
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.995b-1
+ Revision: 718745
- texlive-iwona
- texlive-iwona
- texlive-iwona
- texlive-iwona

