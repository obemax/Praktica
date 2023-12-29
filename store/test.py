from products.models import ProductCategory, Product

# Ваши исходные данные
input_data = """Наименование	Цена	Остаток
Bp		
BP Visco 3000 10W-40 1 л ( 157F38 )	535	8
BP Visco 3000 10W-40 4 л ( 157f36 )	3350			
Castrol
CASTROL трансм 75w90 Syntrans Transaxle 1л ( 1557C3 )	1088	
CASTROL трансм 75w90 Syntrax Universal Plus 1л ( 154FB4 )	1222	
CASTROL трансм Axle Z Limited Slip 90 1л ( 157B18 )	1287	
CASTROL трансм ATF Dex-II Multivehicle 1 л ( 157F42 )	413	
CASTROL трансм ATF Dex-III Multivehicle 1 л ( 157AB3 ) ( 15D676 )	938	3
CASTROL трансм ATF Dex-VI MERKON LV 1л ( 15d747 )	1275	2
CASTROL трансм ATF Dex-VI MERKON LV 4л ( 156CAB )	2893	
CASTROL трансм CVT Transmax 1л ( 156CA5 )	1270	5
CASTROL трансм CVT Transmax 4л ( 156CA6 )	2810	
Castrol Transmax Manual MV 75W90 1л ( 15D816 )	1165	
Масло трансм. Castrol Transmax Manual V 75W80 1л ( 15DF9 )	1081	
CASTROL трансм CVT Transmax 5л ( 15D979 )	6937	
CASTROL Dex-VI MERKON LV Transmax ATF 5л ( 15d978 )	5555	2
CASTROL Масло трансм 75w140 Transmax Limited Slip LL 1л ( 15D998 )	2800	
CASTROL EDGE 0w30 A3/B4 1л ( 157E6A )	1939	
CASTROL EDGE 0w30 A3/B4 4л 157E6B	3856	
CASTROL EDGE 0w40 1л ( 156E8B )	1570	2
CASTROL EDGE 0w40 4л ( 156E8C )	5640	2
CASTROL EDGE 5w30 C3 1л ( 15A569 )	1519	1
CASTROL EDGE 5w30 C3 4л ( 15A568 )	5163	1
CASTROL EDGE 5w30 ll 1л ( 15667C )  15e684	1402	5
CASTROL EDGE 5w30 ll 4л ( 15669A 15668e )	4794	3
CASTROL EDGE 5W40 1л ( 157B1B )	1438	2
CASTROL EDGE 5w40 4л ( 157B1C )	5256	1
CASTROL Magnatec 5w30 1 л ( 15C926 )	1251	10
CASTROL Magnatec 5w30 4 л ( 15C927 )	4804	1
CASTROL Magnatec 5w30 4л+1л 15c928 Акция	2437	
CASTROL Magnatec 5w40 1 л ( 15C9DF )	1250	12
CASTROL Magnatec 5w40 4 л ( 15C9E0 )	4644	2
CASTROL Magnatec Diesel 5w40 4л+1л Акция !!! ( 156EDE )  ( 15E7BD )	5176	2
CASTROL Magnatec 5w40 Diesel 1 л ( 156EDC )	1250	3
CASTROL Magnatec 5w40 Diesel 4 л ( 156EDD )	4813	2
CASTROL GTX 10w40 1л ( 15A4DE )	717	
CASTROL GTX 10w40 4л ( 15A4E0 )	1250	
CASTROL Magnatec 10w40 1 л ( 15CA23 )	825	6
CASTROL Magnatec 10w40 4 л ( 15CA24 )	3000	2
CASTROL Magnatec Diesel 10w40 дизель 1 л ( 15CA2F )	816	2
CASTROL Magnatec Diesel 10w40 дизель 4 л ( 15CA30 )	3000	4
CASTROL Vecton 10w40 E4/E7 20л ( 15BA41 )	6767	
CASTROL Vecton 10w40 E4/E7 4л ( 15B695 )	1500	
CASTROL Vecton 10w40 E4/E7 7л ( 15BA42 )	2570	
CASTROL EDGE 5w30 ll 5л ( 15e78a )	5888	3
CASTROL Magnatec 5w40 4л+1 Акция !!! ( 15C9D8 )	5805	
CASTROL Magnatec Professional Ford 5w30 A5/B5 5л ( 15D5E9 )	6000	
CASTROL Magnatec Professional Ford 5w30 A5/B5 1л ( 15D5E7 )	1563	1
CASTROL Magnatec 5w30 A5 Ford Dualock 4л 15ca3b	5013	
CASTROL Magnatec 5w30 A5 4л+1л ( 15CA3C 15E7BA) Акция	5406	
CASTROL Magnatec 5w30 A5 1л ( 15CA3A )	1360	1
CASTROL Magnatec Professional Ford E 5w20 5л ( 15d633 )	7173	1
CASTROL Magnatec Professional Ford E 5w20 1л ( 15d632 )	1530	1
CASTROL EDGE 0w30 Volvo A5/B5 1л ( 15af76 ) ( ! ! ! литрушками дешевле чем 4л )	1438	8
CASTROL EDGE 0w30 Volvo A5/B5 4л ( 15E3F )	5422	
CASTROL 15049 a 4t  20w50  1л	1128	
CASTROL Magnatec 5w30 A5 4л 15eb41	5013	1
CASTROL Magnatec 5w30 5л ( 15E7B9 )	5474	1
Comma
COMMA 10w40 Eurolite 1л eul1l	675	21
COMMA 10w40 Eurolite 2л ( EUL2L )	1571	
COMMA 10w40 Eurolite 4л ( EUL4L )	2640	8
COMMA 10w40 Eurolite 5л ( EUL5L )	3300	6
COMMA 15w40 XT2000 1л ( XT21L )	399	
COMMA 15w40 XT2000 4л xt24l	1646	0
COMMA 15w40 XT2000 5л ( XT25L )	1968	
COMMA 5w30 Syner-Z 1л syz1l	1100	3
COMMA 5w30 Syner-Z 4л syz4l	3876	2
COMMA 5w30 Syner-Z 5л syz5l	4680	1
COMMA 5w30 XTECH 1л ( XTC1L )	950	7
COMMA 5w30 XTECH 2л xtc2l	1800	1
COMMA 5w30 XTECH 4л ( XTC4L )	3600	9
COMMA Масло моторное 5w30 XTECH 5л ( XTC5L )	4050	9
COMMA 5w40 Syner-G 1л ( SYN1L )	900	23
COMMA 5w40 Syner-G 4л ( SYN4L )	3809	5
COMMA 5w40 Syner-G 5л ( SYN5L )	4020	7
COMMA гидр CHF-11s MVCHF 1л ( CHf1L )	1250	5
COMMA трансм MVATF&PSF 1л mvatf1l	1388	10
Comma 75w90 sx Gl-4 масло трансм. ( SXGl41l )	1100	
Comma 5W30 5l long life ( GML5L )	4636	1
COMMA 5w30 Prolife 5л ( PRO5L )	7092	2
COMMA 5w30 Prolife 1л ( PRO1L )	1000	2
Comma 5w30 4l long life (GML4L )	3744	3
Comma 5w30 1l long life (GML1L )	1201	1
XFP1L Масло моторное COMMA 5W30 X-FLOW 1L	629	
COMMA жидкость ГУР 1л ( PSF1L ) Универсальная с конд. совместима со всеми ATF	1068	3
COMMA 10w40 X-FLOW XS 4л ( XFXS4L )	2480	
COMMA 10w40 X-FLOW XS 5л ( XFXS5L )	1975	
COMMA 5W40 1L PD PLUS DPD1L	967	
COMMA трансм MVATF&PSF 1л mvatf5l	5700	1
Elf	
ELF SPORTI 7 10W40 5л ( 214254 )	2729	
ELF SPORTI 7 10W40 1л ( 214260 )	650	
ELF SPORTI 9 5W30 5л ( 214250 )	3920	
ELF SPORTI 9 5W30 1л ( 214256 )	941	
ELF SPORTI 9 5W40 5л ( 214252 )	3730	
ELF SPORTI 9 5W40 1л ( 208446 )	820	
ELF 10W-40 1 л ( 11110301 )	740	14
ELF 10W-40 4 л ( 10130501 ) ( 11120501 )	2545	7
ELF 10w40 Diesel 1л ( 10140301/11130301 )	866	3
ELF 10w40 Diesel 4л ( 11140501 )	3212	3
ELF 5w30 FULL TECH FE 1л	950	
ELF 5w30 FULL TECH FE 5л ( 213935 ) Валвалайн ( 872771 )	5700	
ELF 5w30 SXR 1 л ( 11070301 )	1463	9
ELF 5w30 SXR 4л ( 10160501 ) ( 11080501 )	4650	
ELF 5W-40 Evolution 900 NF 1л ( 10150301 ) 11050301	1150	13
ELF 5W-40 Evolution 900 NF 4 л ( 10150501 ) ( 11060501 )	4900	1
ELF 5W-40 Evolution 900 SXR 1 л ( 10170301 )	1307	5
ELF 5W-40 Evolution 900 SXR 4 л ( 10170501 ) ( 11100501 ) 10950501	4570	1
ELF трансм 75w80 TRANSELF NFJ 1л ( 194757 213875)	769	
ELF трансм 75w80 TRANSELF NFP 1л ( 195003 ) ( 213974 )	858	
ELF трансм ELFMATIC G3 Dex-III 1л ( 213861 )	844	
ELF трансм 75w TRANSELF NFX 1л ( 223519 )	1140	
ELF 5w30 SXR 5л (213894)	5847	1
ELF EVOLUTION 700 STI 10W40 A3/B4, SN/CF Масло моторное полусинт. (5L) [ELF]	3745	
Eneos
ENEOS Super Gasoline 10W-40 1л ( OIL1354 )	737	2
ENEOS Super Gasoline 10W-40 4л ( OIL 1357 )	2982	3
ENEOS трансм Dex-III 4л	1688	
ENEOS PREMIUM TOURING 5W40 4L ( 8809478942162 )	3683	3
ENEOS ATF MODEL H HONDA Z1/DW-1 Жидкость трансмиссионная ( 4л ) OIL 5078	3720	
ENEOS Premium Touring 5W30 SN 1л ( 8809478942193 )	1168	3
ENEOS Premium Touring 5W30 SN 4л ( 8809478942216 )	3683	3
ENEOS PREMIUM TOURING 5W40 1L  ( 8809478942148 )	1192	3
Ford
FORD 5w30 Formula F 1л ( 15595A )	1408	5
FORD 5w30 Formula F 5л ( 15595E )	5255	6
FORD 5w40 Formula S/SD 1л ( 15b91b )	800	
FORD 5w40 Formula S/SD 5л	6000	
GM
GM 10w40 1л ( 1942043 )	791	7
GM 10w40 5л ( 1942046 / 93165216 )	3763	2
GM 5w30 dexos 2 1л ( 93165690 )	1048	5
GM 5w30 dexos 2 2л ( 1942001 )	2198	
GM 5w30 dexos 2 4л ( 1942002 )	3582	3
GM 5w30 dexos 2 5л ( 1942003 )	3970	4
GM ATF Dexron VI 1940184	1000	
GM 10w40 4л 1942045 93165215	2820	3
GM Россия 5w30 dexos 2 1л ( 95599403 )	492	
GM Россия 5w30 dexos 2 5л ( 95599405 )	2202	
GM Россия 5w30 dexos 2 4л ( 95599404 )	1832	
Honda
HONDA 5w30 Synthetic Blend SN GF-5 0.946l 087989134	1580	2
HONDA 5w30 ULTRA LTD 4л ( 0822899974 )	6300	3
HONDA ULTRA LEO 0w20 4L Масло моторное ( 0822799974 )	5280	5
082069002 HONDA PSF-S Жидкость в гур жел. 354мл	1100	6
Hyundai
HYUNDAI MTF GL4 75w85 1l ( 0430000110 )	1141	10
HYUNDAI MTF GL4 75w90 1l ( 043005L1A0 )	1035	6
HYUNDAI трансм SP-III 1л ( 0450000100 )	1375	12
HYUNDAI трансм SP-III 4л 0450000400	4950	3
HYUNDAI трансм SP-IV 1л ( 0450000115 )	1725	15
HYUNDAI гидр PSF-3 ГУР светло-коричневый 1л 0310000110	1370	1
HYUNDAI гидр PSF-4 (ГУР зеленая) 1л  0310000130	2417	3
HYUNDAI гидр PSF-3 ГУР  1л 0310000100 ( КРАСНАЯ )	1417	2
HYUNDAI 5w30 TURBO SYN 1л ( 0510000141 )	1283	4
HYUNDAI 5w30 TURBO SYN 4л ( 0510000441 )	4725	3
HYUNDAI 5w30 Super Extra 1л ( 0510000110 )	773	3
HYUNDAI 5w30 Super Extra 4л ( 0510000410 )	3088	3
HYUNDAI XTEER 5w30 1л ( 1011002 )	713	6
HYUNDAI XTEER 5w30 4л ( 1041002 )	2645	3
HYUNDAI XTEER 10w40 G500 1л ( 1011044 )	661	2
HYUNDAI XTEER 10w40 G500 4л ( 1041044 )	1938	1
HYUNDAI XTEER 10w40 G700 1л ( 1011009 )	702	2
HYUNDAI XTEER 10w40 G700 4л ( 1041014 )	2317	3
HYUNDAI XTEER 5w40 G700 1л ( 1011136 )	752	1
Hyundai premium DPF 5W30 6l ( 0520000620 )	6400	2
HYUNDAI XTEER Ultra Protection 5W40 1л ( 1011126 )	835	3
HYUNDAI Premium LF 5w20 SM 4л ( 0510000451 )	3600	3
0520000120 Hyundai premium DPF 5W30 1l	1021	4
HYUNDAI XTEER Ultra Protection 5W40 4л ( 1041126 )	3100	3
HYUNDAI PREMIUM LF 5W20 SM Масло моторное синт. 1L ( 0510000151 )	1104	8
HYUNDAI XTEER 5w30 G700 4л ( 1041135 )	2142	2
HYUNDAI XTEER 5w30 6л ( 1061011 )	4083	2
HYUNDAI XTEER 1061126 HYUNDAI XTEER GASOLINE ULTRA PROTECTION 5W40 SP Масло моторное синт. (пластик Корея) (6L)	4560	1
HYUNDAI XTEER 1061136 HYUNDAI XTEER GASOLINE G700 5W40 SP Масло моторное синт. (пластик Корея) (6L)	4163	1
HYUNDAI XTEER 5w30 G700 1л ( 1011135 )	602	2
HYUNDAI XTEER 10w40 G500 6л ( 1061044 )	3245	1
HYUNDAI XTEER 5w30 G700 6л ( 1061135 )	3755	1
Idemitsu
IDEMITSU ATF CVTF 4л 30301201746	4900	4
IDEMITSU ATF CVTF NS1 NS2 1л 3004009175	1435	
IDEMITSU Singapur 0w20 1л ( 30011325724 )	954	2
IDEMITSU Singapur 0w20 4л ( 30011325746 )	3498	2
IDEMITSU Singapur 10w40 1л ( 30015049724 )	1006	6
IDEMITSU Singapur 10w40 4л ( 30015049746 )	3620	15
IDEMITSU Singapur 5w30 1л ( 30011328724 )	1020	5
IDEMITSU Singapur 5w40 4л 30015048746	3650	11
IDEMITSU Singapur 5w30 4л ( 30011328746 )	3678	7
IDEMITSU Singapur 5w40 1л ( 30015048724 )	1063	7
IDEMITSU ZEPRO 0w20 ECO MEDALIST 1л ( 3583001 )	1341	4
IDEMITSU ZEPRO 0w20 ECO MEDALIST 4л ( 3583004 4253004 )	6246	3
IDEMITSU ZEPRO 5w40 EURO SPEC 1л 184900120	1589	8
IDEMITSU ZEPRO 5w40 EURO SPEC 4л ( 1849004 )	5880	
IDEMITSU Zepro Touring 5W-30 1 л ( 1845001 ) (4251001)	1442	18
IDEMITSU трансм Singapur ATF 1л ( 30450248724 )	1148	5
IDEMITSU Zepro Touring 5W-30 4 л ( 1845004 ) ( 4251004 )	4560	7
IDEMITSU трансм Singapur ATF 4л ( 30450248746 )	4450	4
АКЦИЯ !!! IDEMITSU Singapur 0w20 4л+1 30011325-77	2084	
АКЦИЯ !!! IDEMITSU Singapur 5w30 4л+1 30011328-77	2084	
АКЦИЯ !!! IDEMITSU Singapur 5w40 4л+1 30015448-77	2084	
IDEMITSU ZEPRO Diesel DL-1 5W30 C2 4l ( 2156004 )	4738	5
IDEMITSU ZEPRO Diesel DL-1 5W30 C2 1l (2156001)	1357	3
Kixx
KIXX 10w40 G 1л ( SN/CF ) ( 00000086728 )	775	6
KIXX 10w40 G 4л	2481	7
KIXX G1 5W-40 1л ( SP ) ( 00001104677 )	949	5
KIXX G1 5W-40 4л ( SP ) ( 00001104678 )	3038	5
KIXX 10w40 SL/CF 4л ( 00000012067 )	2159	8
KIXX PAO 5W30 1л	853	
KIXX PAO 5W30 4л	3150	
KIXX G1 5W30 (SP) 1л	855	4
KIXX G1 5W30 (SP) 4л  ( 00001104676 )	2736	6
KIXX G1 5W50 (SP) 1л ( 00001107842 )	1027	8
KIXX PAO 5W30 C3 зелен 1л	972	1
KIXX 10w40 SL 1л	675	5
KIXX G1 5W50 (SP) 4л	2985	4
KIXX PAO 5W40 4л	3750	
Liqui Moli		
LIQUI MOLY 10w40 Moligen 1л ( 9059/9955 )	1572	5
LIQUI MOLY 10w40 Molygen 4л ( 9060/8538 )	4958	4
LIQUI MOLY 10w40 Moligen 5l 9061 / 9951	5585	4
LIQUI MOLY 10w40 MoS2 Leichtlauf 1л  1930	1508	1
LIQUI MOLY 10w40 MoS2 Leichtlauf 4л 1917	4585	2
LIQUI MOLY 10w40 MoS2 Leichtlauf 5л 1931 2184	5755	1
LIQUI MOLY 10w40 Optimal 1л ( 3929 )	1135	5
LIQUI MOLY 10w40 Optimal 4л ( 3930 )	3719	5
LIQUI MOLY 10w40 Optimal 5л Акция!!! ( 2287 )	2095	
LIQUI MOLY 10w40 Super Leichtlauf 1л ( 1928 )	1118	1
LIQUI MOLY 10w40 Super Leichtlauf 4л ( 1916 )	4793	1
LIQUI MOLY 10w40 Super Leichtlauf 5л 1929	4766	1
LIQUI MOLY 5w30 Molygen 1л ( 9041 ) 9047	1696	5
LIQUI MOLY 5w30 Molygen 4л ( 9042 )  9089	6289	3
LIQUI MOLY 5w30 Molygen 5л  9043 9952	6784	3
LIQUI MOLY 5w30 Top Tec 4200 1л ( 7660 8972 )	1772	5
LIQUI MOLY 5w30 Top Tec 4200 4л  3715/	6656	4
LIQUI MOLY 5w30 Top Tec 4200 5л ( 7661 8973)	8184	4
LIQUI MOLY 5w30 Top Tec 4600 1л ( 8032 2315 )	1384	5
LIQUI MOLY 5w30 Top Tec 4600 4л ( 3763 )	5191	5
LIQUI MOLY 5w30 Top Tec 4600 5л ( 8033/2316 )	6247	6
LIQUI MOLY 5w40 Molygen 1л 9053	1791	5
LIQUI MOLY 5w40 Molygen 4л 9054	6330	4
LIQUI MOLY 5w40 Molygen 5л 9055/8536	7577	4
LIQUI MOLY 5w40 Molygen 5л Акция!!! 39023	4315	
LIQUI MOLY 5w40 Optimal 1л ( 3925 )	1282	5
LIQUI MOLY 5w40 Optimal 4л ( 3926 )	4860	5
LIQUI MOLY 5w40 Optimal 5л Акция!!! ( 2293 )	2968	
LIQUI MOLY 5w40 Synthoil High Tech 1л  1924 1855	1796	2
LIQUI MOLY 5w40 Synthoil High Tech 4л ( 1915 / 2194 )	6480	2
LIQUI MOLY 5w40 Synthoil High Tech 5л ( 1925 / 1856 )	7158	2
LIQUI MOLY 5w40 Top Tec 4100 1л ( 7500 / 9510 )	1514	5
LIQUI MOLY 5w40 Top Tec 4100 4л ( 7547 ) 2195	5530	6
LIQUI MOLY 5w40 Top Tec 4100 5л ( 7501/9511 )	6825	5
LIQUI MOLY 5w30 Molygen New Generation 5л Акция!!! ( 39029 )	5460	
LIQUI MOLY 10w40 Molygen New Generation 5л Акция!!! ( 39028 )	5030	
LIQUI MOLY 5w30 Optimal 1л ( 39000 )	1347	5
LIQUI MOLY 5w30 Optimal 4л ( 39001 )	4488	5
LIQUI MOLY 5w30 Special Tec AA 1л ( 7515 7615 )	1450	5
LIQUI MOLY 5w30 Special Tec AA 4л ( 7516 / 7616 )	5328	5
LIQUI MOLY 5w30 Special Tec LL 4л ( 7654 )	5552	4
LIQUI MOLY 5w30 Special Tec LL 1л ( 8054 / 2447 )	1488	5
LIQUI MOLY 5w30 Special Tec LL 5л ( 8055 ) 2448	6252	4
LIQUI MOLY 5w30 Special Tec F 1л ( 8063 / 2325)	1458	5
LIQUI MOLY 5w30 Special Tec F 5л ( 8064 2326 )	6255	5
LIQUI MOLY 5w30 Optimal HT Synth 5л вместо 4л АКЦИЯ!!!! ( 39010)	3000	
LIQUI MOLY 5w30 Special Tec AA 5л ( 7530 )	6050	6
LIQUI MOLY 5w40 Leichtlauf High Tech 1л ( 8028 ) ( 2327 )	1393	5
LIQUI MOLY 5w40 Leichtlauf High Tech 5л ( 8029 / 2328 )	6196	5
LIQUI MOLY 5w30 Synthoil High Tech 1л ( 9075 20957 )	1651	3
LIQUI MOLY 5w30 Synthoil High Tech 4л ( 9076 / 20958 )	6570	2
LIQUI MOLY 5w30 Synthoil High Tech 5л ( 9077/ 20959 )	7406	2
LIQUI MOLY 5W40 Top Tec 4100 5л АКЦИЯ!!!!!! ( 39041 )	6413	
LIQUI MOLY 5W30 Top Tec 4200 5л АКЦИЯ!!!!!! ( 39042 )	6943	
LIQUI MOLY 0w20 Special Tec AA 1л ( 8065 )	1554	5
LIQUI MOLY 0w20 Special Tec AA 4л ( 8066/9705 )	5443	6
LIQUI MOLY 5W30 Special Tec AA 5л АКЦИЯ!!!!! ( 39043 )	5517	
LIQUI MOLY 0W30 Leichtlauf Longtime 1л ( 39038 )	1400	
LIQUI MOLY 0W30 Leichtlauf Longtime 4л ( 39039 )	5650	2
LIQUI MOLY 0w30 Leichtlauf Longtime 5л ( 39040 )	6199	2
LIQUI MOLY 5w30 Special Tec DX1 1л ( 20967 )	1401	5
LIQUI MOLY 5w30 Special Tec DX1 4л ( 20968 )	5496	3
LIQUI MOLY 5w30 Special Tec DX1 5л ( 20969 )	6153	1
9952A АКЦИЯ LiquiMoly НС-синт. мот.масло Molygen New Generation 5W-30 SP GF-6A (5л) + 8787R*1	7481	3
LM 85w90 GL5 трансм 1л 8039 1410	1589	3
LIQUI MOLY Мин.Трансм.Масло Hypoid-Getrieboil 85W-90 Gl4 1л ( 1954 1030 )	1218	3
LIQUI MOLY Мин.Трансм.Масло Hypoid-Getrieboil 85W-90 Gl5 1л ( 1956 1035 )	1190	3
LIQUI MOLY Мин.Трансм.Масло Top Tec MTF 5100 75W Gl4 1л ( 20842 )	2140	7
LIQUI MOLY HC-синт.Трансм.Масло Top Tec MTF 5200 75W-80 Gl4 1л ( 20845 )	2240	5
LIQUI MOLY HC-синт.Трансм.Масло АКПП Top Tec ATF 1800 1л ( 2381 )	1460	5
LIQUI MOLY HC-синт.Трансм.Масло АКПП Top Tec ATF 1800 5л ( 39020 / 20662/ 3687)	6523	2
LIQUI MOLY П/С трансм.Масло Hypoid-Getrieboil TDL 75W-90 Gl4/Gl5 4л ( 3939 )	4300	
LIQUI MOLY П/С трансм.Масло Hypoid-Getrieboil TDL 75W-90 Gl4/Gl5 1л ( 3945 1407 )	1894	5
LIQUI MOLY Синт.Трансм.Масло  75W-90 GL4+ 1л ( 3979 / 4434 )	2249	4
LIQUI MOLY HC-синт.Трансм.Масло АКПП Top Tec ATF 1200 1л ( 7502 3681 )	1569	5
LIQUI MOLY HC-синт.Трансм.Масло АКПП Top Tec ATF 1200 5л ( 8040 3682 )	7871	2
LM жидкость гидравлическая универсальная 1л ( 3978 )	2226	1
LIQUI MOLY Синт. тр.масло Vollsynthetisches Getrieb. 75W-90 GL-5 (1414)	2343	3
LIQUI MOLY Масло Hypoid getriebeoil 80w90 GL-5 1Л ( 4406 )	1422	3
LIQUI MOLY CVT Top Tec ATF 1400 1л ( 3662 )	1842	8
LiquiMoly НС-синт. тр.масло д/АКПП Top Tec ATF 1100 (1л) 3651	1336	5
LiquiMoly НС-синт. тр.масло д/DSG  8100 5л ( 20626 )	7845	1
LiquiMoly НС-синт. тр.масло д/DSG 8100 1л ( 3640 )	1884	5
21359 LiquiMoly Синт. тр.масло Top Tec MTF 5300 70W-75W GL-4 (1л)	2551	9
LM П/С Мот. масло 2T 2-Takt-Motoroil TC 1л ( 3958 / 1052 )	1202	5
LM HC-синт. Мот. масло 4T ATV Motoroil Offroad 10W40 SN MA2 1л ( 7540 )	1270	3
LM HC-синт. Мот. масло 4T ATV Motoroil Offroad 10W40 SN MA2 4л ( 7541 )	4348	2
LM синт. Мот, масло 4T Motorbike Offroad 10W40 SN MA2 4л ( 3056 )	4557	1
LM синт. Мот. масло 4T Motorbike Street 10W40 SN MA2 4л ( 7512 1243 )	4758	2
LM синт. Мот. масло 4T Motorbike Street 10W40 SN MA2 1л ( 7609 / 1521 )	1399	5
LM синт. Мот.масло 4T Motorbike Offroad 10W40 SN MA2 1л ( 3055 )	1262	2
LM синт. Мот.масло 4T Motorbike Street 15W50 SL MA2 4л ( 1689 )	4115	2
LM синт. Мот. масло 4T Motorbike Street 15W50 SL MA2 1л ( 2555 )	1322	2
LM Мин. тр. масло д/скутеров 80w-90 GL-4 0,15л ( 1680 )	458	1
LM синт. Мот. масло д/мотоц Mtorrad Gear Oil 75w-90 0.5л (7589 )	1240	1
LM синт. Мот. масло 4T Motorbike Synth Street Race 10W40 SN MA2 1л ( 20753 )	1629	2
LM синт. Мот. масло 4T Motorbike Synth Street Race 10W40 SN MA2 4л ( 20754 )	6681	1
LM синт. Мот. масло 4T Motorbike Synth Street Race 10W50 SN MA2 4л ( 7508 )	6543	1
LM синт. Мот. масло 4T Motorbike Synth Street Race 10W50 SN MA2 1л ( 3982 )	1717	2
LM Мин. Мот. масло 10W30 4T д/газон. Gardengerate-oil ( 8037/1273 )	1116	3
LM мот.масло д/мотоц Racing Gear Oil 80W 0.5l ( 1617 )	676	1
LM Motorbike fork oil medium 10W 1L ( 2715 )	1707	1
LM Motorbike fork oil medium 10w для вилок и амортизаторов 0,5л 7599 1506	989	2
LIQUI MOLY вилочное масло Racing fork Oil Light 5W 0.5 л ( 1523 )	902	2
LIQUI MOLI вилочное масло Motorad fork Oil Light 5W 1л ( 2716 )	1706	1
LM синт. Мот, масло 2T Motorbike Semisynth Scooter TC FC 1л ( 3983 1621 ) Racing Scooter	1236	5
LM Масло д/скутеров 2Т мин Motorrad Scooter Basic 1л ( 8068/1619 )	1141	5
LiquiMoly Мин. мот.масло д/4-т.мотоц. Motorbike 4T Street 20W-50 SN ( 1500 ) Plus MA2 (1л)	1185	2
LiquiMoly Мин. мот.масло д/4-т.мотоц. Motorbike 4T Street 20W-50 SN Plus MA2 ( 1696 )(4л)	3764	2
Mannol		
MANNOL DEXRON II 4l ( 1331 )	1794	3
MANNOL 10w40 Classic 1л	579	1
MANNOL 10w40 Classic 4л	2046	1
MANNOL 10w40 Classic 5л ( 1155 )	2272	1
MANNOL 10w40 Molibden Benzin 1л ( 1120 )	525	3
MANNOL 10w40 Molibden Benzin 4л 1121  75054	2010	3
MANNOL 5w40 Extreme 1л	649	2
MANNOL 5w40 Extreme 4л	2090	2
MANNOL мото 2т п/с 1л  ( 1404 )	625	6
MANNOL мото 4т п/с 1л (1400)	573	1
MANNOL мото 4т п/с 4л (1425)	1935	4
MANNOL для компрессоров  1л  1918	649	6
MANNOL MAXPOWER масло трансм. GL5 75W140 1л ( 1236 )	874	2
MANNOL Racing+ester 10w60 4л ( 4037 )	2474	1
MANNOL CHF Гидравлическая жидкость 1л (2472=8990)	1048	
MANNOL DEXTRON 3 4л ( 1356 )	1636	
MANNOL DEXRON II 1L ( 1330 )	470	5
MANNOL 10w60 Racing+ester 1л ( 4036 )	700	2
MANNOL MTF-4 GL-4 75w80 1л  ( 1943 )	995	5
MANNOL ELITE 5W40 PAO Масло моторное Синтетическое 4л ( 1006 )	2987	1
MANNOL 10w40 Classic 7л ( 1992 )	3500	1
MANNOL ELITE 5W40 PAO Масло моторное Синтетическое 1л ( 1005 )	839	1
MANNOL Масло трансмиссионное 1л GL4/GL-5 75W90 (1304 )	767	5
MANNOL Масло трансмиссионное 4л  75W90 GL-4/GL5 ( 1353 )	2659	2
Mazda		
MAZDA Ultra 5w30 1л ( 053001TFE )	1525	
MAZDA Original Ultra 5w30 5л ( 053005TFE )	6000	
MAZDA Ultra 5w30 DPF 1л	650	
Mercedes		
Mercedes 5w40 MB229.5 1л ( A000989210711faer )	1800	
Mercedes 5w40 MB229.5 5л ( A000989790213BIFR )	6000	
Mercedes 5w40 MB229.5 1л ( A000989860611AAEE )	1553	10
Mitsubishi		
MITSUBISHI 5w30 пластик п/с 1л ( MZ320363 )	710	
MITSUBISHI 5w30 пластик п/с 4л ( MZ320364 )	5131	2
MITSUBISHI 5w30 пластик синт 1л ( MZ320756 )	945	
MITSUBISHI 5w30 пластик синт 4л ( MZ320757 )( MZ321036 )	5288	2
MITSUBISHI трансм SP-III 1л mz320159  ( mz320215 )	1496	2
MITSUBISHI трансм SP-III 4л 4024610 железо	3794	2
MITSUBISHI 5w30 пластик синт 1л ( mz321035 ) синг	1426	7
Mobil		
Mobil трансм ATF LT 71141 1л ( 152648 )	1500	
Mobil трансм ATF 3309 трансм 1л (153519)	1600	
Mobil трансм ATF 220 1л 152647	920	3
Mobil трансм ATF 320 1л	920	
Mobil трансм 75w90 MOBILUBE 1 SHC 1л 152659	850	
Mobil трансм 80w90 GX GL-4 1л	540	
Mobil трансм ATF Multi-Vehicle 1л ( 156095 )	1200	1
Mobil 0w40 New Life 1л ( 153691 )	1917	
Mobil 0w40 New Life 4л (153692 )	5263	
Mobil 5w30 ESP Formula 1л ( 154279 )	2280	
Mobil 5w30 ESP Formula 4л ( 154285 )	6770	
Mobil 5w40 1 FS X1 1л ( золот кр ) 153266	1830	1
Mobil 5w40 1 FS X1 4л ( золот кр ) 153265	4385	
Mobil 1 FS 5w50 1л ( 153631 )	1375	3
Mobil 5w50 4л ( 153638 )	4689	
Mobil 5w30 Super 3000 Formula FE 1л ( 152565 )	1314	
Mobil 5w30 Super 3000 Formula FE 4л ( 152564 )	4500	
Mobil 5w40 Super 3000 1л ( 152567 150012 )	1065	1
Mobil 5w40 Super 3000 4л ( 152566 )	3876	5
Mobil 10w40 Super 2000 1л ( 152569 )	833	
Mobil 10w40 Super 2000 4л ( 152568 )	2997	
Mobil 1 X1 A5 B5 5w30 4l ( 154806 )	5500	
Mobil 5w30 Super 3000 Formula FE 5л Акция!!! ( 156155 )	4500	
Mobil 1 X1 A5 B5 5w30 1l ( 152722 154805)	1097	
Mobil 5w40 Super 3000 5л Акция!!! ( 156154 )	5414	1
Mobil 5w30 PROMO ESP Formula 5л ( 155145)	5980	
Mobil 1 FS 5w30 PROMO 5л ( 155144)	4257	
Mobil 1 X1 A5 B5 5w30 5l PROMO ( 155143 )	3488	
Mobil 1 FS 5w30 1л ( 153749 )	1830	
Mobil 5w30 ESP Formula 5л ( 154294 )	6750	
Mobil 5w40 Super 3000 5л  ( 150565 )	5107	
Mobil Ultra (Esso)		
Mobil Ultra 10w40 1л ( 152625 )	650	
Mobil Ultra 10w40 4л ( 152624 )	2100	
Motul		
MOTUL 4100 10w40 Turbolight 1л ( 108644 )	794	2
MOTUL 4100 10w40 Turbolight 4л ( 109462 )	3317	
MOTUL 6100 10w40 Synergie +Technosynthese 1л (108646 )	924	
MOTUL 6100 10w40 Synergie +Technosynthese 4л ( 109463)	3238	
MOTUL 8100 5w30 Eco-Clean+ 1л ( 101580 )	1100	1
MOTUL 8100 5w30 Eco-Clean+ 5л 101584	3950	1
MOTUL 8100 5w30 Eco-Clean 1л ( 101542 )	1209	13
MOTUL 8100 5w30 Eco-Clean 5л ( 101545 )	5312	
MOTUL 8100 5w30 Eco-Nergy 1л ( 102782 111685 )	1322	2
MOTUL 8100 5w30 Eco-Nergy 4л ( 104257 111860 )	5131	1
MOTUL 8100 5w30 Eco-Nergy 5л ( 102898 111686 )	5131	3
MOTUL 8100 5w30 X-Clean+ 5л 106377 111684	6107	1
MOTUL 8100 5w30 X-Clean EFE 1л ( 109470 111687 )	1587	4
MOTUL 8100 5w30 X-Clean EFE 5л ( 109471 111688 )	6810	2
MOTUL 8100 5w30 X-Clean EFE 4л ( 109171 )	4920	1
MOTUL 8100 5w40 X-CESS GEN2 1л ( 109774 ) 102784	1274	1
MOTUL 8100 5w40 X-CESS GEN2 4л ( 109775 )	5016	1
MOTUL 8100 5w40 X-CLEAN GEN2 1л ( 109761 )	1307	5
MOTUL 8100 5w40 X-Clean 4л ( 112119 )	5107	2
MOTUL 8100 5w40 X-Clean GEN2 5л ( 109762 )	4472	
MOTUL 8100 X-CESS 5w40 GEN2 5л ( 109776 /102870/111682 )	5016	
MOTUL Specific 5w30 DEXOS2 1л ( 102638 )	1200	1
MOTUL Specific 5w30 DEXOS2 5л 102643	6300	1
MOTUL Specific 5w30 MB229.51 1л	843	
MOTUL Specific 5w30 MB229.51 5л	1000	
MOTUL Specific 5w30 RN 0720 1л 102208	1423	
MOTUL Specific 5w30 RN 0720 5л 102209	6630	
MOTUL Specific 5w30 504.00 507.00 1л ( 106374 )	1200	3
MOTUL Specific 5w30 504.00 507.00 5л ( 106375 )	5637	
MOTUL Specific 5w40 BMW LL-04 1л	778	
MOTUL Specific 5w40 502.00 505.01 1л ( 101573 )	1200	1
MOTUL Specific 5w40 502.00 505.01 5л ( 101575 )	6300	
MOTUL 8100 5w30 X-Clean+ 1л ( 106376 )	1344	1
MOTUL 8100 ECO-LITE 5w30 5л ( 108214 )	5050	
MOTUL 8100 ECO-LITE 5w30 1л ( 108212 )	1188	
MOTUL 6100 SYN-CLEAN 5w40 1л ( 107941 )	995	1
MOTUL 8100 5w40 X-CLEAN GEN2 5л АКЦИЯ!!!!! ( 109373 )	1568	
MOTUL 6100 SYN-NERGY 5W30 5л ( 107972 ) АКЦИЯ!!! 1л в подарок	3985	
MOTUL 6100 SYN-CLEAN 5W40 5л ( 107943 ) АКЦИЯ!!! 1л в подарок	2453	
MOTUL 6100 SYN-NERGY 5W30 1л ( 107970 )	957	1
MOTUL 6100 SYN-NERGY 5W40 1л ( 107975 111689 )	942	4
MOTUL 6100 SYN-NERGY 5W40 4л ( 107978 )	3305	1
Ро MOTUL 4100 10w40 Turbolight ( 108634 ) бочка	550	
MOTUL 8100 0W20 ECO-LITE 1л ( 108534 )	1270	2
MOTUL 8100 0W20 ECO-LITE 4л ( 108535 )	4665	2
MOTUL 8100 0W20 ECO-LITE 5л ( 108536 )	6485	2
MOTUL 6100 SYN-CLEAN 5w40 4л ( 107942 )	3466	1
MOTUL 8100 ECO-LITE 5w30 4л ( 108213)	3879	
MOTUL 6100 SYN-NERGY 5W30 4л ( 107971 )	3769	
MOTUL 2t Outboard Tech 1л ( 102789 )	1200	
MOTUL мото 2t Garden 1л ( 106280 )	989	
MOTUL мото 2t Scooter Expert 1л ( 105880 )	1199	5
MOTUL мото 2t Scooter Power 1л 105881	1612	1
MOTUL мото 4t 10w40 5100 1л ( 104066 ) 106906	1272	2
MOTUL мото 4t 10w40 5100 4л ( 104068 ) 104177	4928	1
MOTUL мото 4t 10w40 7100 1л ( 104091 ) 104202	1818	1
MOTUL мото 4t 10w40 7100 4л ( 104092 )	7062	1
MOTUL мото 4t Scooter Expert 1л ( 105960 )	1181	2
MOTUL мото 4t Scooter Power 1л  105958	1414	10
MOTUL 2t Outboard Tech 2л ( 101726 )	2712	1
MOTUL 4t Garden SAE 30 1л ( 102787 )	818	2
MOTUL гидр Multi HF 1л ( 106399 )	1700	
MOTUL трансм 75w80 Motylgear GL-4 GL-5 1л ( 105782 )	1409	3
MOTUL трансм 75w80 Motylgear GL-4 GL-5 2л ( 101155 )	2959	
MOTUL трансм 75w90 Gear300 1л ( 105777 )	2181	
MOTUL трансм 75w90 Gear300 LS 1л ( 105778 )	1575	
MOTUL трансм 75w90 Motylgear 1л ( 109055 )	1077	1
MOTUL трансм 80w90 Gearbox 1л ( 105787 )	957	
MOTUL трансм 80w90 HD 1л ( 105781 )	811	
MOTUL трансм Multi ATF 1л ( 105784 )	1435	4
MOTUL трансм Dex-||| 1л ( 105776 )	1100	2
MOTUL трансм Dex-||| 2л ( 100318 )	2100	
MOTUL трансм ATF VI 1л ( 105774 ) 112145	1600	9
MOTUL трансм Multi CVTF 1л ( 105785 )	1715	8
MOTUL трансм Multi DCTF 1л ( 105786 )	1655	6
Nissan		
NISSAN 10w40 пластик 1л ( ke90099932 )	1188	2
NISSAN 10w40 пластик 5л ( ke90099942r )	5139	2
NISSAN 5w30 железн 1л ( KLAN505301 )	1553	4
NISSAN 5w30 железн 4л ( KLAN505304 )	5093	4
NISSAN 5w30 пластик 1л ( KE90099933R )	1113	
NISSAN 5w30 пластик 5л ( KE90099943R )	5873	
NISSAN 5w40 пластик 1л ( KE90090032 )	1500	2
NISSAN 5w40 пластик 5л ( KE90090042R )	6300	
NISSAN NS-2 CVT трансмис вариатор 4л ( KLE5200004EU )	7208	2
NISSAN NS-3 CVT трансмис вариатор 4л ( kle5300004 )	7698	2
NISSAN ATF Matic-D 1л ( ke90899931 )	1000	
NISSAN ATF Matic-J 1л ( KE90899932R )	2115	
Shell		
SHELL HX7 10w40 1л	840	
SHELL HX7 10w40 4л	2625	4
SHELL HX7 10w40 Diesel 1л	700	
SHELL HX7 10w40 Diesel 4л	2850	
SHELL HX7 10w40 ро бочка 1л	470	0
SHELL HX7 5w30 1л	1287	
SHELL HX7 5w30 4л	3276	
SHELL HX7 5w40 1л	1215	3
SHELL HX7 5w40 4л  ( 550051497 )	3088	1
SHELL HX8 5w30 1л	1250	3
SHELL HX8 5w30 4л	3950	3
SHELL HX8 5w30 A5/B5 1л	1313	
SHELL HX8 5w30 A5/B5 4л	4075	
SHELL HX8 5w40 1л	1125	
SHELL HX8 5w40 4л	4100	
SHELL Motor Oil 10w40 1л	550	
SHELL Motor Oil 10w40 4л	1932	
SHELL ULTRA 0w30 ECT 1л	1984	
SHELL ULTRA 0w30 ECT 4л	5000	
SHELL ULTRA 5w30 ECT 1л	1020	8
SHELL ULTRA 5w30 ECT 4л	6000	
SHELL ULTRA 5w40 1л	1250	2
SHELL ULTRA 5w40 4л	4407	3
SHELL трансм Spirax s6 ATF 1л lspi089b11	610	
SHELL ULTRA 0w30 ECT 4л+1л Акция	5500	
SHELL ULTRA 0w40 4л	4850	
SHELL ULTRA 0w40 1л	1764	
SHELL Helix High Mileage 5w40 4л	3230	
SHELL Helix High Mileage 5w40 1л	838	
SHELL ULTRA 5w30  1л	1132	4
SHELL ULTRA 5w30  4л	4417	4
SHELL Helix Ultra Racing 10w60 SN/CF A3/B4 4л	5200	
SHELL Helix Ultra Racing 10w60 SN/CF A3/B4 1л	1000	
SHELL трансм Spirax s3 ATF III MD3 1л	500	
SHELL трансм Spirax s4 AT 75w90 1л	657	
SHELL трансм Spirax s3 ATF III MD3 4л	1625	
SHELL трансм Spirax s6 ATF 4л lspi089b12	1901	
SHELL ECO 5w40 4л	3105	
SHELL ECO 5w40 1л	1000	
SHELL трансм Spirax s4 AT 75w90 4л	2225	
SHELL трансм Spirax s4 G 75w90 1л	905	
SHELL HELIX ULTRA ECT 5w30 ро бочка 1л	975	0
SHELL Helix High Mileage 5w40 4л+1л АКЦИЯ !	4389	
SHELL ULTRA 5w30 ECT 4л+1л АКЦИЯ !	5300	
SHELL HX8 5w40 4л+1л АКЦИЯ !	4120	
SHELL HX8 5w30 4л+1л АКЦИЯ !!!	4320	
SHELL ULTRA 5w30 4л+1л АКЦИЯ!	3325	
SHELL RIMULA R6 M 10W40 20л	9000	
SHELL ULTRA 5w40 5л  (550052838)	5017	1
Total Quartz
TOTAL CLASSIC 7 10W40 5л ( 213691 )	2800	
TOTAL CLASSIC 7 10W40 1л ( 213752 )	710	
TOTAL CLASSIC 9 5W40 5л ( 213696 )	4100	
TOTAL CLASSIC 9 5W40 1л ( 213730 )	930	
TOTAL CLASSIC 9 5W30 5л ( 213839 )	4399	
TOTAL CLASSIC 9 5W30 1л ( 213786 )	618	
TOTAL 10 w40 7000 1 л ( 11010301 )	928	7
TOTAL 10w40 7000 4л ( 11020501 )	2615	6
TOTAL 10w40 7000 дизель 1л ( 10740301 ) ( 11030301 )	802	3
TOTAL 10w40 7000 дизель 4л ( 10740501 ) ( 11040501 )	3263	3
TOTAL 5w30 Energy HKS 9000 1л ( 213799 )	1283	
TOTAL 5w30 Energy HKS 9000 5л ( 213800 ) Валвалайн ( 885853 )	6474	
TOTAL 5w30 9000 Future NFC 1 л ( 10980301 )	1168	7
TOTAL 5w30 9000 Future NFC 4л ( 10990501 )	4600	
TOTAL 5w30 Ineo ECS 1л ( 11200301 )	1542	
TOTAL 5w30 Ineo ECS 4л ( 11210501 )	4020	7
TOTAL 5w30 INEO MC3 Dexos2 1л	1320	
TOTAL 5w30 INEO MC3 Dexos2 4л	6240	
TOTAL 5w40 9000 1л ( 10210301 ) ( 10940301 )	1293	20
TOTAL 5w40 9000 4л ( 10210501 )	4237	9
TOTAL трансм 75w90 TRANS DUAL 9 FE 1л ( 10350301 11150301 )	1495	4
TOTAL трансм Gear 8 75w80 1л ( 214082 )	657	
TOTAL 5w40 9000 1л бочка ( 10211101 )	770	
TOTAL CLASSIC 9 5w30 бочка ( 208L) 213718	770	
TOTAL QUARTZ 9000 FUTURE NFC 5w30 (208L) 10231101 бочка	887	
TOTAL 5w30 INEO MC3 Dexos2 5л	6200	
Toyota		
"Toyota  0888602105 TOYOTA CVT TC Жидкость трансмиссионная АКПП вариаторного типа (железо/Япония) (4L)"	5060	2
TOYOTA 0w20 железо Япония 1л ( 0888013206 )	1403	1
TOYOTA 5w30 железо 1л ( 0888013706 )	1494	3
TOYOTA 5w30 железо 4л ( 0888013705 )	4844	6
TOYOTA 5w40 1л ( 0888080376GO )	903	
TOYOTA 5w40 5л ( 0888080375GO )	4150	
TOYOTA трансм ATF WS 4л 0888602305	6430	2
TOYOTA трансм TYPE T-IV 1л ( 0279000T46S )	801	
TOYOTA трансм TYPE T-IV 4л ( 0888681015 )	5539	2
TOYOTA 0W20 4l железо Япония ( 0888013205 )	6000	2
TOYOTA 5w30 пластик 1л ( 0888080846 )	1164	1
TOYOTA 5w30 пластик 5л ( 0888080845 )	5856	1
0888602505 TOYOTA CVT FE Жидкость трансмиссионная АКПП вариаторного типа (железо Япония) (4L)	6188	2
Vag		
Vag 5w40 Special D дизель 1л G052505m2	935	
Vag 5w40 Special G бенз 1л ( GR52502M2 )	1006	
Vag 5w40 Special G бенз 5л ( GR52502M4 )	6000	
VAG гидр PSF ГУР зеленый 1л ( G004000M2 )	2630	
VAG трансмис для раздатки 1л G052536A2	2000	
Vag G052180A2 VAG ATF	1800	
Valvoline
VALVOLINE трансм GEAR OIL GL4  75w90 1л ( 867064 )	1300	
VALVOLINE трансм GEAR OIL GL4 /GL4+  75w80 1л ( 866895 )	1250	17
VALVOLINE трансм AXLE OIL GL5  75w90 1л ( 866890 )	1187	5
VALVOLINE трансми AXLE OIL GL5 LS 75w90 1л ( 866904 )	1339	5
VALVOLINE трансм GEAR OIL 75w 1л ( 886573 )	1200	1
VALVOLINE трансм ATF DEX/MERC NEW 1л ( 866913 )	803	6
VALVOLINE 10w40 All Climate 1л	541	3
VALVOLINE 10w40 All Climate 4л	2631	
VALVOLINE 10w40 All Climate 5л  872776	3654	1
VALVOLINE 10w40 Maxlife 1л ( 872295 )	1011	30
VALVOLINE 10w40 Maxlife 4л ( 872296 )	3336	4
VALVOLINE 10w40 Maxlife 5л ( 872297 )	4122	7
VALVOLINE 5w40 Maxlife 1л (872363)	1050	27
VALVOLINE 5w40 Maxlife 4л ( 872364 )	3500	
VALVOLINE 5w40 Synpower 1л	1021	
VALVOLINE 5w40 Synpower 4л	3853	
VALVOLINE 5w40 Synpower 5л ( 872382 )	4633	4
VALVOLINE 5w30 Synpower 1л ( 872377 )	1184	12
VALVOLINE 5w30 Synpower 4л ( 872378 )	3853	
VALVOLINE 10w40 All Climate 5л Акция!!! 5 по цене 4	2077	
VALVOLINE 10w40 Maxlife 5л Акция!!! 5 по цене 4   872327	2122	
VALVOLINE 10w40 SYN POWER 5л Акция!!! 5 по цене 4	2210	
VALVOLINE 5w40 All Climate 5л ( 872281 )	3590	1
VALVOLINE 10w40 Synpower 1л ( 872271 )	880	1
VALVOLINE 5w40 SYN POWER 5л Акция!!! 5 по цене 4 ( 872383 )	2737	
VALVOLINE 5w40 Maxlife 5л АКЦИЯ 5 по цене 4!!!	3581	
VALVOLINE 10w40 Maxlife 5л Акция!!! 5 по цене 4 872327		
VALVOLINE 5w40 All Climate 5л Акция!!! 5 по цене 4	2300	
VALVOLINE 5w40 All Climate 1л ( 872282 )	832	
VALVOLINE 5w30 Synpower XL-III C3 1л ( 872372 )	1177	3
VALVOLINE 5w30 Synpower XL-III C3 4л ( 872373 )	4405	
VALVOLINE 5w30 Synpower XL-III C3 5л ( 872375 )	5484	
VALVOLINE 5w30 Synpower MST C4 5л ( 872771 )	6114	2
VALVOLINE 5w30 Synpower MST C4 1л ( 872770 )	1163	2
VALVOLINE 5w30 Synpower FE 5л ( 872552 )	5176	3
VALVOLINE 5w30 Synpower FE 1л ( 872551 )	890	
VALVOLINE 10w40 Synpower 4л ( 872260 )	3458	1
VALVOLINE 10w40 Synpower 5л ( 872259 )	4289	1
VALVOLINE 5w30 Synpower MST C3 5л ( 874308 )	5159	2
VALVOLINE 5w30 Synpower MST C3 1л ( 8723596 )	1131	
VALVOLINE 5w30 Maxlife 1л ( 872371 )	1051	
VALVOLINE 5w30 Maxlife 4л ( 872370 )	4141	7
VALVOLINE 5w30 Maxlife 5л ( 872794 )	4248	
Xado		
XADO 10w40 Energy Drive 1л	1250	4
XADO 10w40 Energy Drive 4л	3875	4
XADO 5w40 1л	1300	
XADO 5w40 4л	3700	
XADO Atomic oil 10w40 SL/CF 4л (xa 28244)	3250	
ХАDО Atomic Oil ATF III/IV/V синтетическое масло для АКПП ( XA 20129 )	1413	
Zic
ZIC трансм PSF-3 Жидкость ГУР 1л ( 132661 )	782	5
ZIC трансм 75w85 G-FF Gl-4 1л ( 132626 )	777	5
ZIC трансм 75w85 G-FF Gl-4 4л ( 162626 )	2390	4
ZIC трансм 75w85 G-F TOP GL-4 1л ( 132624 )	1016	5
ZIC трансм 75w85 G-F TOP GL-4 4л	3420	2
ZIC трансм 75w90 G-F TOP 1 л ( 132629 )	1054	5
ZIC трансм 75w90 G-F TOP 4л ( 162629 )	3165	2
ZIC трансм 80w90 G5 Gl-5 1л ( 132633 )	747	5
ZIC трансм 80w90 G5 Gl-5 4л ( 162633 )	2342	4
ZIC трансм 80w90 G-EP Gl-4 1л 132625	709	5
ZIC трансм 80w90 G-EP Gl-4 4л ( 162625 )	2335	3
ZIC трансм ATF Dex-II 1л ( 132623 )	830	2
ZIC трансм ATF Dex-II 4л ( 162623 )	2493	2
ZIC трансм ATF Dex-III 1л ( 132632 )	830	4
ZIC трансм ATF Dex-III 4л 162632	2674	2
ZIC трансм ATF Dex-VI 1л 132630	975	5
ZIC трансм ATF Dex-VI 4л ( 162630 )	3052	2
ZIC трансм SP-3 1л ( 132627 )	1016	5
ZIC трансм SP-3 4л ( 162627 )	3345	8
ZIC трансм SP-4 1л ( 132646 )	1067	5
ZIC трансм SP-4 4л ( 162646 )	3338	7
ZIC ATF Multi Жидкость трансмис. для АКПП 1л ( 132628 )	895	5
ZIC масло трансм ATF MULTI LF 4л ( 162665 )	3055	5
ZIC масло трансм ATF MULTI LF 1л ( 132665 )	966	5
ZIC ATF Multi HT Масло трансм. 4л ( 162664 )	2938	3
ZIC ATF Multi 4l жидкость трансм. для АКПП ( 162628 )	2777	4
ZIC ATF Multi HT Масло трансм. 1Л ( 132664 )	976	5
ZIC MULTI CVT 1л ( 132631 )	1268	5
ZIC MULTI CVT 4л ( 162631 )	4000	2
ZIC трансм 75w90 G-F TOP розлив  1л	800	0
ZIC DCTF MULTI 1Л синтетика ( 132685 )	1341	5
ZIC мото M7  2T синт 1л ( 137213 )	561	
ZIC мото M7 4T 10w40 синт 1л ( 132027 )	725	5
ZIC мото M9 4T 10w40 синт 1л ( 132026 )	759	5
ZIC мото M9 Racing Edition 10w50 синт 1л ( 137214 )	937	5
ZIC 5w40 X9 1л ( 132000 )	1142	5
ZIC 5w40 X9 4л ( 162613 )	3575	6
ZIC 10w40 X5 1л ( 132622 )	636	3
ZIC 10w40 X5 4л ( 162622 )	2069	5
ZIC 10w40 X5 6л ( 172622 )	3300	2
ZIC 10w40 X5 дизель 1л ( 132660 )	690	3
ZIC 10w40 X5 дизель 4л 162660	2129	4
ZIC 10w40 X5000 6л	2146	
ZIC 10w40 X7 LS 1л ( 132620 )	715	4
ZIC 10w40 X7 LS 4л ( 162620 )	2329	6
ZIC 10w40 X7 LS 6л ( 172620 )	3746	3
ZIC 10w40 X7 Diesel 1л ( 132607 )	742	8
ZIC 10w40 X7 Diesel 4л ( 162607 )	2228	4
ZIC 10w40 X7 Diesel 6л 172607	3931	2
ZIC 10w40 X7 LS розлив 1л	550	138
ZIC 10w40 X5 дизель 6л 172660	3074	2
ZIC 5w30 X9 4л ( 162614 )	3682	7
ZIC 5w30 X9 1л ( 132614 )	1177	5
ZIC TOP 5w30 4л ( 162681 )	4235	4
ZIC TOP 5w30 1л ( 132681 )	1353	5
ZIC ZERO 0w30 4л ( 162676 )	4290	2
ZIC ZERO 0w30 1л ( 132676 )	1356	3
ZIC 5w30 X7 LS 1л ( 132619 )	877	3
ZIC 5w30 X7 LS 4л ( 162619 )	2888	2
ZIC 5w30 X7 LS 6л ( 172619 )	4415	
ZIC TOP 0W40 4л ( 162611 )	4568	2
ZIC TOP 0W30 4Л ( 162680 )	4995	3
ZIC TOP 0W30 1Л ( 132680 )	1576	3
ZIC TOP 0W40 1л ( 132900 / 132611 )	1465	2
ZIC 5W30 X9 FE A5/B5 4l ( 162615 )	3562	6
ZIC 5w30 X9 FE A5/B5 1л ( 132615 )	1138	4
ZIC TOP 5w40 4л ( 162682 )	4111	4
ZIC TOP 5w40 1л ( 132682 )	1314	5
ZIC TOP LS 5w30 1л ( 132612 LS )	1379	5
ZIC TOP LS 5w30 4л ( 162612 LS )	4317	7
ZIC ZERO 0w20 4л ( 162035 )	3958	5
ZIC ZERO 0w20 1л ( 132035 )	1302	5
ZIC 5w30 LS X9 4л ( 162200 )	3798	7
ZIC 5w30 LS X9 1л ( 132608 / 132200 )	1199	5
Газпромнефть		
Газпромнефть G-Energy Expert G  10w40  1л	240	
Газпромнефть G-Energy Expert G  10w40  4л	917	
Газпромнефть G-Energy F Synth  5w40  1л	450	
Газпромнефть G-Energy F Synth  5w40  4л	1961	
Газпромнефть G-Energy Synthetic Active  5w40  1л	403	
Газпромнефть G-Energy Synthetic Active  5w40  4л	1850	
Газпромнефть G-Energy Synthetic Long Life  10w40  1л	641	
Газпромнефть G-Energy Synthetic Long Life  10w40  4л	1300	
Газпромнефть Premium L 10w40  1л	342	3
Газпромнефть Premium L 10w40  4л	1288	6
Газпромнефть Premium N  5w40  1л	545	3
Газпромнефть Premium N  5w40  4л	2200	4
Газпромнефть Super 10w40  SG/CD 1л	300	7
Газпромнефть Super 10w40 SG/CD 4л G2389901318	1127	4
Газпромнефть МГЕ-46В 20л		
Газпромнефть трансм 80w90 GL-4 1л	256	
Газпромнефть трансм 80w90 GL-4 4л	973	
Газпромнефть трансм 80w90 GL-5  1л	439	2
Газпромнефть трансм 80w90 GL-5 4л	1492	1
Газпромнефть Super 10w40  SG/CD 5л	1408	3
Газпромнефть Standard 20w50 1л	240	1
Газпромнефть Standard 20w50 5л	1041	
Газпромнефть Super 15w40 1л	256	
Газпромнефть Super 15w40 5л	1080	
Газпромнефть G-Energy S Synth 10w40 1л	347	
Газпромнефть G-Energy S Synth 10w40 4л	1520	
Газпромнефть G-Energy Synthetic Active 5w30 1л	457	
Газпромнефть G-Energy Synthetic Active 5w30 4л	1560	
Газпромнефть G-Energy Synthetic Super Start 5w30 1л	454	
Газпромнефть G-Energy Synthetic Super Start 5w30 4л	1720	
Газпромнефть Premium L 10w40 5л	1555	3
Газпромнефть G-Energy Expert G 10w40 4л+1л в подарок!!!	1578	2
Газпромнефть G-Energy Synthetic Active 5w30 4л+1л в подарок !!!	2383	2
Газпромнефть G-Energy Synthetic Active 5w40 4л+1л в подарок !!!	2391	1
Gazpromneft G-Energy Far East 5W30 4л ( A253141935 )	1754	
G 253142285 Масло GAZPROMNEFT G-MOTION 4T 10w30 1l	471	22
G 2389901372 Масло GAZPROMNEFT MOTO 2T 1l мото	344	9
Газпромнефть G-Energy Expert L 10w40 4л+1л в подарок!!!	1651	
Газпромнефть G-Energy Synthetic Super Start 5w30 4л+1Л в подарок!!!	2669	
Газпромнефть Premium L 10w40  4+1л в подарок	1288	2
Газпромнефть Diesel Premium 10w40  5L A3/B4	1957	1
Газпромнефть Premium N  5w40  4+1л в подарок	2083	1
Лукойл		
Масло МОТО ЛУКОЙЛ 2Т МГД-14М 4л ( Страна происхождения товара - Россия ) 19557	1063	8
Масло МОТО ЛУКОЙЛ 2Т МГД-14М 1л ( Страна происхождения товара - Россия ) 19556	296	20
ЛУКОЙЛ Супер SG/CD 5w40 1л (19441)	310	3
ЛУКОЙЛ Супер SG/CD 5w40 4л (19442)	1294	2
ЛУКОЙЛ Genesis Universal 10w40 1л (3148644)	563	38
ЛУКОЙЛ Genesis Universal 10w40 4л (3148646)	1850	43
ЛУКОЙЛ Genesis 5w30 ARMOTECH JP 1л ( 3149900 )	700	17
ЛУКОЙЛ Genesis 5w30 ARMOTECH JP 4л ( 3149902 )	2800	6
ЛУКОЙЛ Genesis 5w30 ARMOTECH SN/CF A3/B4 HK 4л ( 3149287 )	3019	10
ЛУКОЙЛ Genesis 5w30 ARMOTECH diesel 1л ( 3149148 )	716	4
ЛУКОЙЛ Genesis 5w30 ARMOTECH diesel 4л ( 3149855 )	2800	7
ЛУКОЙЛ Genesis 5w40 ARMOTECH 1л ( 3148670 )	800	9
ЛУКОЙЛ Genesis 5w40 ARMOTECH 4л ( 3148675 )	2800	46
ЛУКОЙЛ Genesis 5w40 ARMOTECH SPECIAL розлив бочка 1 л ( 1599897 )	600	0
ЛУКОЙЛ Авангард Ультра 10w40  п/с  18л	4378	
ЛУКОЙЛ Авангард Ультра 10w40  п/с  5л	1725	39
ЛУКОЙЛ Авангард Ультра 15w40  мин  18л	4550	
ЛУКОЙЛ Авангард Ультра 15w40 мин 5л ( 1552345 )	1792	7
ЛУКОЙЛ Люкс 10w40 1л ( 19187 )	364	5
ЛУКОЙЛ Люкс 10w40 4л ( 19188 )	1163	14
ЛУКОЙЛ Люкс 10w40 5л (19299)	1410	14
ЛУКОЙЛ Люкс 10w40 розлив 1л	280	0
ЛУКОЙЛ Люкс 5w40 п/с 1л ( 19189 )	460	5
ЛУКОЙЛ Люкс 5w40 п/с 4л ( 19190 )	1472	5
ЛУКОЙЛ Люкс 5w40 синт 1л ( 207464 )	656	5
ЛУКОЙЛ Люкс 5w40 синт 4л ( 207465 )	2100	7
ЛУКОЙЛ Супер 10w40 1л ( 19191 )	300	17
ЛУКОЙЛ Супер 10w40 4л ( 19192 )	1070	8
ЛУКОЙЛ Супер 10w40 5л ( 19193 )	1298	8
ЛУКОЙЛ Супер 10w40 розлив бочка 1л	250	149
ЛУКОЙЛ Супер 15w40 1л ( 19194 )	314	4
ЛУКОЙЛ Супер 15w40 4л (19195)	1071	2
ЛУКОЙЛ Супер 15w40 5л (19196)	1240	1
ЛУКОЙЛ АВАНГАРД 15w40  мин  18л  187781	3637	
ЛУКОЙЛ АВАНГАРД 15w40 мин. 5л ( 19309 )	1293	
ЛУКОЙЛ Genesis 5w30 ARMOTECH FD 4л 3149878	2582	10
ЛУКОЙЛ Супер SG/CD 5w40 5л (19443)	1364	1
ЛУКОЙЛ Genesis 5w30 ARMOTECH FD 1л ( 3149867 )	900	13
ЛУКОЙЛ Genesis 5w30 ARMOTECH SN/CF A3/B4 HK 1л ( 3149286 )	926	40
ЛУКОЙЛ Genesis 5w30 ARMOTECH DX1 1л ( 3173878 )	684	5
ЛУКОЙЛ Genesis 5w30 ARMOTECH DX1 4л ( 3173877 )	2600	3
3186380 Масло гидравлическое ЛУКОЙЛ ГЕЙЗЕР СТ 32 20л (16кг)	4709	4
ЛУКОЙЛ Авангард Ультра 10w40 п/с 20л ( 3052073 )	6280	
ЛУКОЙЛ GENESIS 10w40 SPECIAL ADVANCED 216.5 розлив ( 3148649 )	450	0
ЛУКОЙЛ Genesis Universal 5w40 4л ( 3148631 )	1862	2
ЛУКОЙЛ-АВАНГАРД Ультра 10w40 розлив 1л ( 200л бочка )	350	0
ЛУКОЙЛ Авангард Ультра 15w40 мин 20л ( 3052075 )	6494	
ЛУКОЙЛ Genesis 5w30 A5/B5 SPECIAL розлив бочка 1 л (1599892 )	600	0
ЛУКОЙЛ Genesis 5w30 ARMOTECH GC 4л ( 3149300 )	3473	7
ЛУКОЙЛ Genesis 5w30 ARMOTECH GC 1л ( 3149368 )	1086	5
ЛУКОЙЛ Genesis 5w40 ARMOTECH Diesel 1л (3150233 )	687	8
ЛУКОЙЛ Genesis 5w40 ARMOTECH Diesel 4л ( 3149129 )	2198	8
Масло ЛУКОЙЛ-АВАНГАРД УЛЬТРА SAE 10W40 API CI-4/SL 206л	288	206
ЛУКОЙЛ Авангард Ультра 10w40 п/с 50л	15592	
ЛУКОЙЛ Genesis Universal 5w40 1л ( 3148630 )	738	2
ЛУКОЙЛ GENESIS GC 0w20 1Л ( 3409225)	1270	5
ЛУКОЙЛ GENESIS GC 0w20 4Л ( 3409230)	3978	5
Лукойл Авангадр Ультра Моторное масло 10w40 60л ( 55л ) ( 0279000T46S )	16982	
ЛУКОЙЛ Genesis 0w20 ARMOTECH JP 1л ( 3149924 SPX )	870	13
ЛУКОЙЛ Genesis 0w20 ARMOTECH JP 4л ( 3149925 SPX )	2784	6
ЛУКОЙЛ Genesis CN 5w40 1л ( 3473441 )	2500	1
ЛУКОЙЛ Люкс 5w40 п/с 5л ( 19300 )	1821	2
ЛУКОЙЛ трансм 75w90 GL-4 1л (19531)	655	7
ЛУКОЙЛ трансм 75w90 GL-4 4л ( 19532 )	2245	3
ЛУКОЙЛ трансм 75w90 GL-5 1л ( 3556187 )	760	7
ЛУКОЙЛ трансм 75w90 GL-5 4л п/с ( 19545 )	2751	5
ЛУКОЙЛ трансм 80w90 GL-4 1л ( 19539 )	404	1
ЛУКОЙЛ трансм 80w90 GL-4 4л ( 3524536 )	1402	8
ЛУКОЙЛ трансм 80w90 GL-5 1л ( 19550 )	410	8
ЛУКОЙЛ трансм 80w90 GL-5 4л ( 3524251 )	1400	6
ЛУКОЙЛ трансм ATF Dex-III 1л ( 191352 ) 3289604	598	7
ЛУКОЙЛ трансм ATF Dex-III 4л ( 191353 )	2120	2
OIL RIGHT		
OIL RIGHT 15w40 1л ( 2362 )	167	3
OIL RIGHT 15w40 5л 2360	717	4
OIL RIGHT Веретенка И-20А 1л	160	4
OIL RIGHT Веретенка И-20А 5л ( 2592 )	584	2
OIL RIGHT Веретенка И-20А 10л 2591	1132	6
OIL RIGHT Веретенка И-20А 20л   2588	2335	7
OIL RIGHT Веретенка И-40А 1л	183	
OIL RIGHT Веретенка И-40А 5л	615	1
OIL RIGHT Веретенка И-40А 20л	3620	1
ОЙЛ РАЙТ ТАД-17 80W-90 1 л ( 2547 )	185	2
ОЙЛ РАЙТ ТАД-17 80W-90 3 л 2546	493	2
ОЙЛ РАЙТ ТАД-17 80W-90 5 л ( 2545 )	757	5
ОЙЛ РАЙТ ТАД-17 80W-90 10 л (2544)	1438	7
OIL RIGHT ТСП-15К трансм масло 10л ( 2548 )	1880	3
OIL RIGHT М10Г2К 10л 2501	1295	9
OIL RIGHT Веретенка И-40А 10л	1193	2
OIL RIGHT трансм ТЭП-15в нигрол 3л ( 2553 )	385	4
OIL RIGHT М10Г2К 1л ( 2504 )	218	10
OIL RIGHT M8B 20w20 5л 2484	647	4
OIL RIGHT ТЭП-15В Трансм. масло 5л ( 2555 )	614	4
OIL RIGHT М10Г2К 5Л ( 2502 )	718	4
800429 Масло Волга ойл ВМГ3 5Л	950	
ОЙЛ РАЙТ МГЕ-46В 5Л ( 2602 ) гидравлическое масло	761	8
ОЙЛ РАЙТ МГЕ-46В 10Л ( 2601 ) гидравлическое масло	1317	1
OIL RIGHT ВМГЗ гидр масло 10л ( 2628 )	1532	4
ОЙЛ РАЙТ МГЕ-46В 20Л ( 2600 ) гидравлическое масло	3237	
OIL RIGHT трансм ТЭП-15в нигрол 1л ( 2554 )	150	2
3TON		
3TON Country 2t с дозатором 1л st508 (55263)	317	
3TON PSF Жидкость ГУР. 1л ( 40267 )	212	3
LUXE		
LUXE масло моторное 20w50 1л ( 368 )	232	4
LUXE масло моторное 20w50 5л ( 366 )	1042	
LUXE ATF Dexron III 1 л ( 559 )	337	17
LUXE ATF Dexron III 4 л ( 558 )	1262	2
LUXE масло моторное 20w50 4л ( 367 )	969	3
LUXE ATF Dexron II 1 л ( 560 )	323	5
LUXE ATF Dexron II 4 л ( 561 )	1118	2
COUNTRY		
COUNTRY 2t 0,1л 55295	100	
COUNTRY 2t 0,5л ( 40239 )	185	3
COUNTRY Масло  2t 1л ( 40238 )	280	37
COUNTRY 4t 1л ( 40242 )	284	26
COUNTRY компрессорное  ST 506  1л  40221	247	6
COUNTRY 3TON Масло цепное для бензопил ST300 0.5л  ( 40235 )	125	2
NGN		
NGN Premium 10W40 1л масло моторное ( V172085606 v272085606 )	744	1
V172085302 NGN GOLD 5w40 4литра	4041	2
NGN GOLD 5w40 Синт. бочка 1л	600	
NGN Масло моторное 10W40 4л ( V172085306 )	2659	
V172085602 NGN GOLD 5W40 1ЛИТР	1122	2
KAMA OIL		
Масло моторное КАМА OIL 10/40 п/синт. 4л	821	
Масло моторное КАМА OIL 10/40 п/синт . 1 л	202	1
Масло моторное КАМА OIL 10/40 п/синт 5 л	900	
FEBI Жидкость ГУР мин.зел. 1L ( 06162 )	1135	1
FEBI Жидкость ГУР син.зел. 1L ( 06161 )	1574	5
VENDOR 15385373 REZOIL Масло ULTRA 2-т. дозатор п синт. API TC 0,946 л.,	726	
RAVENOL трансмис масло PSA SAE 75w80 1л ( 122210000101999 )	1561	5
ENI I-RIDE SCOOTER 2T полусинтетическое моторное масло 1л (152296)	1030	2
ENI I-RIDE RACING 2T синтетическое моторное масло 1л (154181)	1250	2
Rolf		
ROLF 5w40 1л (322234 )	843	2
ROLF 5w40 GT API SN/CF 4 л ( 322229 )	2594	2
ROLF 10w40 Dynamic SJ/CF 1л	487	2
ROLF 10w40 Dynamic SJ/CF 4л	1800	2
ROLF 10w40 Energy SL/CF 1л	600	2
ROLF 10w40 Energy SL/CF 4л ( 322227 )	1952	2
ROLF 5w30 GT 4 л  (322620)	2310	3
ROLF 5w30 GT SAE API SN/CF 1 л ( 322446 )	739	2
ROLF 5w30 3-Synthetic ACEA C3 4 л ( 322729 )	3368	1
ROLF 5w30 3-Synthetic ACEA C3 1 л ( 322728 )	1080	1
ROLF 10W40 Energy SL/CF 4+1 АКЦИЯ!!!!!!	1750	
ROLF 5W30 GT SN/CF 4+1 АКЦИЯ !!!!!!  ( 322403 )	2310	
ROLF 5W40 GT SN/CF 4+1 АКЦИЯ !!!!!!  ( 322405 )	2245	
ROLF 10w40 Energy SL/CF 4л ( Акция  )	1757	
Sintec		
Моторное масло Sintec 10W40 СУПЕР 4л	1260	
Моторное масло Sintec 10W40 СУПЕР 5л	1213	
Моторное масло Sintec 5W30 Platinum Син. 1л (600143)	565	4
Моторное масло Sintec 5W30 Platinum Син. 4л  ( 801939 )	1736	2
Моторное масло Sintec 5W40 Platinum Син. 4л	1736	
Моторное масло Sintec 5W40 Platinum Син. 1л ( 600138 )	565	1
Моторное масло Sintec 10W40 СУПЕР 1л	200	
Моторное масло Sintec 10W40 люкс АКЦИЯ!!!! 5л по цене 4л	1134	1
Моторное масло Sintec 5W40 Platinum Син. АКЦИЯ !!!!! 5л ПО ЦЕНЕ 4л	1835	2
Моторное масло Sintec 10W40 люкс 4л ( 600232 )	1120	2
Моторное масло Sintec 10W40 люкс 1л ( 801942 )	339	5
Моторное масло Sintec 5W30 Platinum Син. АКЦИЯ !!!!! 5л ПО ЦЕНЕ 4л	1806	1
SINTEC  Моторное масло EXTRALIFE 5000 SAE 10W-40 1л API SL/CF	496	2
Suzuki		
SUZUKI ECSTAR 5W30 1L ( 99M0022R02001 )	1117	2
SUZUKI ECSTAR 5W30 4L ( 99M0022R02004 )	5020	1
Роснефть		
Роснефть MAGNUM ULTRATEC 5W40 4l ( 40815442 )	2048	2
Роснефть MAGNUM MAXTEC 5W-40 4l ( 40814642 )	1800	3
40813832 Роснефть MAGNUM COLDTEC 5W-40 1l	550	
РОСНЕФТЬ 15w40 SG/CD 4л (40814442)	873	
РОСНЕФТЬ 20w50 SG/CD 4л (40814542)	887	
Роснефть Maximum 10W40 216.5л Масло мотор. Розлив	200	0
Роснефть MAGNUM COLDTEC (SN/CF) 5W30 5l	1944	2
Роснефть MAGNUM COLDTEC (SN/CF) 5W30 1l	500	12
Роснефть MAGNUM ULTRATEC (SN/CF) 5W40 1l	623	9
Роснефть Gidrotec OE HLP-46 20л   (40840260)	3310	9
РОСНЕФТЬ масло гидравлическое МГЕ-46 20л  (40633169)	2475	9
Роснефть И-20 Масло  без тары 1л (2302)	94	0
Роснефть Масло моторное SAE 30  M-10Г2К 20л   (10134)	2424	5
Роснефть Масло моторное ВМГЗ 20л   ( 40633069 )	2550	3
Роснефть Масло моторное М-10ДМ 20л ( 12083 )	2894	4
Роснефть MAGNUM ULTRATEC 10W40 4l ( 40814942 )	1645	3
Роснефть MAGNUM ULTRATEC (SL/CF) 5W30 4+1l  ( 00000107765 )	1975	2
Роснефть MAGNUM ULTRATEC 5W40 ( SN/CF ) 4l +1 L ( 00000107762 )	2079	
Роснефть MAGNUM ULTRATEC A3 (SN/CF) 5W40 4 l  (0000084360)	2109	1
Роснефть MAGNUM ULTRATEC A5 (SN/CF) 5W30 4 l (00000112144)	2277	1
Роснефть MAGNUM ULTRATEC FE (SN/CF) 5W30 4 l ( 00000107640)	2208	1
Роснефть трансмиссионное 80w90 мин GL-5 4L (00001134465 )	1346	1
Роснефть трансмиссионное 80W90 мин GL-4 4L (00001134469)	1401	1
Роснефть MAGNUM ULTRATEC 10W40 4l +1l	1663	1
LUBEX		
LUBEX Масло моторное ROBUS PRO 10W40 20л ( L01907720020 )	9304	1
Татнефть		
Татнефть Ультра Оптима 10w40 4л	1337	
Татнефть Ультра Оптима 10w40 РОЗЛИВ	300	10
Татнефть LUXE 5w40 4л ( 000001490 )	2100	8
Татнефть LUXE 5w40 1л ( 0000001489 )	572	6
Татнефть LUXE 5w30 4л ( 4650229680819 )	1644	
Татнефть LUXE 5w30 1л ( 0000001488 )	533	
Татнефть TANECO DeLuxe Eco Special Synth 5w30 4л ( 0000001470 )	2347	3
Татнефть TANECO DeLuxe Eco Special Synth 5w30 1л ( 0000001469 )	671	2
Татнефть TANECO Premium Ultra Eco Synth 5w30 1л ( 0000001465 )	720	4
Татнефть TANECO Premium Ultra Eco Synth 5w30 10л	5688	
Татнефть TANECO Premium Ultra Synth 5w40 4л  (4650229680024)	2100	7
Татнефть TANECO Premium Ultra Synth 5w40 1л ( 4650229680031 )	579	7
Татнефть TANECO Premium Ultra Synth 5w30 1л ( 0000001504 )	579	3
Татнефть TANECO Premium Ultra Synth 5w30 4л ( 0000001463 )	2100	2
Татнефть TANECO Premium Ultra Synth 5w40 10л ( 0000001600 )	4173	
Татнефть TANECO DeLuxe Special Diesel Siynth 10w40 10л ( 4650229681915 )	4400	
TANECO Premium ECO Ultra Synth 5W30 1л (синтетика) РОЗЛИВ	600	0
Татнефть LUXE PAO 5w30 4л ( 4650229680864 )	2265	4
Татнефть LUXE PAO 5w40 4л ( 4650229680857 )	2351	3
Татнефть LUXE PAO 5w30 10л ( 4650229681359 )	5880	
Татнефть LUXE PAO 5w40 1л ( 4650229680840 )	674	3
Татнефть TANECO DeLuxe Eco Special Synth 5w30 10л ( 4650229681731 )	4813	
Татнефть LUXE PAO 5w30 1л ( 4650229680871)	673	2
Bardahl		
Bardahl 5w40 XTC 4l 36162	4642	2
BARDAHL 36311 5W30 XTC SN 1L	1288	3
BARDAHL XTS 5w30 SL/CF A5/B5 100% синт 1л ( 36541 )	1294	2
BARDAHL Масло моторное 10W40 XTC SN/CF 1L п/с (36241)	954	2
BARDAHL 5W40 XTC SN/CF 1L синт. ( 36161 )	1207	2
BARDAHL 5W40 XTC SN/CF 5L син. ( 36163 )	5305	1
BARDAHL XTS 5w30 SL/CF A5/B5 100% синт 5л ( 36543 )	6187	2
BARDAHL  36313 5W30 XTC SN 5L	5912	1
BARDAHL 36312 5W30 XTC SN 4L	5169	1
BARDAHL Масло моторное 10W40 XTC SN/CF 4L п/с (36242)	3415	1
BARDAHL Масло моторное 10W40 XTC SN/CF 5L п/с ( 36243 )	4191	1
BARDAHL Масло моторное 5W30 XTS SL/CF 4L синт ( 36542 )	5045	3
Opet		
OPET мот.масло Fullmax 5W-40 1л ( 601214806 )	871	5
OPET мот.масло Fullmax 5W-30 A5 B5 (1л) (601214868)	863	5
OPET мот.масло Fullmax 5W-30 A5 B5 4л (601214875)	3194	5
OPET мот.масло Fulllife S 10W-40 1л ( 601215094 )	729	5
OPET мот.масло Fulllife S 10W-40 4л ( 601215100 )	2831	4
OPET мот.масло Fulllife S 10W-40 5л (601439957)	3431	2
OPET Синт. мот.масло Fullmax 5W-40 SN 4л ( 601214813A )	3255	4
FAVORIT		
FAVORIT SUPER Масло моторное 10w40 бочка1л (фаворит)	200	
FAVORIT Premium Масло моторное 5w30 1л ( FV37021E )	410	
FAVORIT Premium Масло моторное 5w30 4л ( FV37024E )	1533	
FAVORIT Premium Масло моторное 5w40 1л ( FV37011E )	391	
FAVORIT Premium Масло моторное 5w40 4л ( FV37014E )	1400	
FAVORIT Premium Масло моторное 10w40 1л ( FV35101E )	250	
FAVORIT Premium Масло моторное 10w40 4л ( FV35104E )	862	
Totachi		
TOTACHI NIRO LV SN/CF 10w40 полусинт 4l ( 19604 )	2000	2
TOTACHI NIRO LV SN/CF 10w40 полусинт 1l ( 19601 )	557	1
TOTACHI NIRO OPTIMA 10W40 SL/CF 1л Масло моторное полусинт. ( 1C401 )	500	1
TOTACHI NIRO OPTIMA 10W40 SL/CF 4л Масло моторное полусинт. ( 1C404 )	1794	2
TOTACHI NIRO LV SN 5W30 Акция 4л+1л в подарок ( 1G104 )	2594	1
TOTACHI NIRO LV SN/CF 5W40 Акция 4л + 1л в подарок ( 1G204 )	2363	2
ReinWell		
ReinWell Моторное масло 5W-40 А3/В4 1л ( 4932 )	591	5
ReinWell Моторное масло 5W-40 А3/В4 4л ( 4933 )	2300	5
ReinWell Моторное масло 10W-40 A3/B4 1л ( 4957 )	489	5
ReinWell Моторное масло 10W-40 A3/B4 4л ( 4958 )	1695	5
ReinWell Моторное масло 5W-30 A5/B5 1л ( 4942 )	626	5
ReinWell Моторное масло 5W-30 A5/B5 4л + Пакет ( 4953A АКЦИЯ )	2454	5"""

# Разделение данных по строкам и столбцам
rows = [line.split('\t') for line in input_data.split('\n')]

# Исключение пустых строк
filtered_rows = [row for row in rows if row]

# Преобразование данных в желаемый формат (список словарей)
header = filtered_rows[0]
data = []
category = ''

for row in filtered_rows[1:]:
    if len(row) > 1 and row[1]:
        if not row[2]:
            row[2] = 0
        data.append(dict(zip(header + ['Категория'], row[:3] + [category])))
    else:
        category = row[0]

# Вывод результата

for item in data:
    print(item)

for item in data:
    # Получение или создание категории
    category, created = ProductCategory.objects.get_or_create(name=item["Категория"])

    # Создание продукта
    product = Product.objects.create(
        name=item["Наименование"],
        description='',
        price=item["Цена"],
        quantity=item["Остаток"],
        category=category
    )
    # Дополнительные действия, если необходимо
    product.save()
