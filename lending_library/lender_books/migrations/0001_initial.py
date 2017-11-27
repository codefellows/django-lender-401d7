# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-27 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('year', models.IntegerField(choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900), (1899, 1899), (1898, 1898), (1897, 1897), (1896, 1896), (1895, 1895), (1894, 1894), (1893, 1893), (1892, 1892), (1891, 1891), (1890, 1890), (1889, 1889), (1888, 1888), (1887, 1887), (1886, 1886), (1885, 1885), (1884, 1884), (1883, 1883), (1882, 1882), (1881, 1881), (1880, 1880), (1879, 1879), (1878, 1878), (1877, 1877), (1876, 1876), (1875, 1875), (1874, 1874), (1873, 1873), (1872, 1872), (1871, 1871), (1870, 1870), (1869, 1869), (1868, 1868), (1867, 1867), (1866, 1866), (1865, 1865), (1864, 1864), (1863, 1863), (1862, 1862), (1861, 1861), (1860, 1860), (1859, 1859), (1858, 1858), (1857, 1857), (1856, 1856), (1855, 1855), (1854, 1854), (1853, 1853), (1852, 1852), (1851, 1851), (1850, 1850), (1849, 1849), (1848, 1848), (1847, 1847), (1846, 1846), (1845, 1845), (1844, 1844), (1843, 1843), (1842, 1842), (1841, 1841), (1840, 1840), (1839, 1839), (1838, 1838), (1837, 1837), (1836, 1836), (1835, 1835), (1834, 1834), (1833, 1833), (1832, 1832), (1831, 1831), (1830, 1830), (1829, 1829), (1828, 1828), (1827, 1827), (1826, 1826), (1825, 1825), (1824, 1824), (1823, 1823), (1822, 1822), (1821, 1821), (1820, 1820), (1819, 1819), (1818, 1818), (1817, 1817), (1816, 1816), (1815, 1815), (1814, 1814), (1813, 1813), (1812, 1812), (1811, 1811), (1810, 1810), (1809, 1809), (1808, 1808), (1807, 1807), (1806, 1806), (1805, 1805), (1804, 1804), (1803, 1803), (1802, 1802), (1801, 1801), (1800, 1800), (1799, 1799), (1798, 1798), (1797, 1797), (1796, 1796), (1795, 1795), (1794, 1794), (1793, 1793), (1792, 1792), (1791, 1791), (1790, 1790), (1789, 1789), (1788, 1788), (1787, 1787), (1786, 1786), (1785, 1785), (1784, 1784), (1783, 1783), (1782, 1782), (1781, 1781), (1780, 1780), (1779, 1779), (1778, 1778), (1777, 1777), (1776, 1776), (1775, 1775), (1774, 1774), (1773, 1773), (1772, 1772), (1771, 1771), (1770, 1770), (1769, 1769), (1768, 1768), (1767, 1767), (1766, 1766), (1765, 1765), (1764, 1764), (1763, 1763), (1762, 1762), (1761, 1761), (1760, 1760), (1759, 1759), (1758, 1758), (1757, 1757), (1756, 1756), (1755, 1755), (1754, 1754), (1753, 1753), (1752, 1752), (1751, 1751), (1750, 1750), (1749, 1749), (1748, 1748), (1747, 1747), (1746, 1746), (1745, 1745), (1744, 1744), (1743, 1743), (1742, 1742), (1741, 1741), (1740, 1740), (1739, 1739), (1738, 1738), (1737, 1737), (1736, 1736), (1735, 1735), (1734, 1734), (1733, 1733), (1732, 1732), (1731, 1731), (1730, 1730), (1729, 1729), (1728, 1728), (1727, 1727), (1726, 1726), (1725, 1725), (1724, 1724), (1723, 1723), (1722, 1722), (1721, 1721), (1720, 1720), (1719, 1719), (1718, 1718), (1717, 1717), (1716, 1716), (1715, 1715), (1714, 1714), (1713, 1713), (1712, 1712), (1711, 1711), (1710, 1710), (1709, 1709), (1708, 1708), (1707, 1707), (1706, 1706), (1705, 1705), (1704, 1704), (1703, 1703), (1702, 1702), (1701, 1701), (1700, 1700), (1699, 1699), (1698, 1698), (1697, 1697), (1696, 1696), (1695, 1695), (1694, 1694), (1693, 1693), (1692, 1692), (1691, 1691), (1690, 1690), (1689, 1689), (1688, 1688), (1687, 1687), (1686, 1686), (1685, 1685), (1684, 1684), (1683, 1683), (1682, 1682), (1681, 1681), (1680, 1680), (1679, 1679), (1678, 1678), (1677, 1677), (1676, 1676), (1675, 1675), (1674, 1674), (1673, 1673), (1672, 1672), (1671, 1671), (1670, 1670), (1669, 1669), (1668, 1668), (1667, 1667), (1666, 1666), (1665, 1665), (1664, 1664), (1663, 1663), (1662, 1662), (1661, 1661), (1660, 1660), (1659, 1659), (1658, 1658), (1657, 1657), (1656, 1656), (1655, 1655), (1654, 1654), (1653, 1653), (1652, 1652), (1651, 1651), (1650, 1650), (1649, 1649), (1648, 1648), (1647, 1647), (1646, 1646), (1645, 1645), (1644, 1644), (1643, 1643), (1642, 1642), (1641, 1641), (1640, 1640), (1639, 1639), (1638, 1638), (1637, 1637), (1636, 1636), (1635, 1635), (1634, 1634), (1633, 1633), (1632, 1632), (1631, 1631), (1630, 1630), (1629, 1629), (1628, 1628), (1627, 1627), (1626, 1626), (1625, 1625), (1624, 1624), (1623, 1623), (1622, 1622), (1621, 1621), (1620, 1620), (1619, 1619), (1618, 1618), (1617, 1617), (1616, 1616), (1615, 1615), (1614, 1614), (1613, 1613), (1612, 1612), (1611, 1611), (1610, 1610), (1609, 1609), (1608, 1608), (1607, 1607), (1606, 1606), (1605, 1605), (1604, 1604), (1603, 1603), (1602, 1602), (1601, 1601), (1600, 1600), (1599, 1599), (1598, 1598), (1597, 1597), (1596, 1596), (1595, 1595), (1594, 1594), (1593, 1593), (1592, 1592), (1591, 1591), (1590, 1590), (1589, 1589), (1588, 1588), (1587, 1587), (1586, 1586), (1585, 1585), (1584, 1584), (1583, 1583), (1582, 1582), (1581, 1581), (1580, 1580), (1579, 1579), (1578, 1578), (1577, 1577), (1576, 1576), (1575, 1575), (1574, 1574), (1573, 1573), (1572, 1572), (1571, 1571), (1570, 1570), (1569, 1569), (1568, 1568), (1567, 1567), (1566, 1566), (1565, 1565), (1564, 1564), (1563, 1563), (1562, 1562), (1561, 1561), (1560, 1560), (1559, 1559), (1558, 1558), (1557, 1557), (1556, 1556), (1555, 1555), (1554, 1554), (1553, 1553), (1552, 1552), (1551, 1551), (1550, 1550), (1549, 1549), (1548, 1548), (1547, 1547), (1546, 1546), (1545, 1545), (1544, 1544), (1543, 1543), (1542, 1542), (1541, 1541), (1540, 1540), (1539, 1539), (1538, 1538), (1537, 1537), (1536, 1536), (1535, 1535), (1534, 1534), (1533, 1533), (1532, 1532), (1531, 1531), (1530, 1530), (1529, 1529), (1528, 1528), (1527, 1527), (1526, 1526), (1525, 1525), (1524, 1524), (1523, 1523), (1522, 1522), (1521, 1521), (1520, 1520), (1519, 1519), (1518, 1518), (1517, 1517), (1516, 1516), (1515, 1515), (1514, 1514), (1513, 1513), (1512, 1512), (1511, 1511), (1510, 1510), (1509, 1509), (1508, 1508), (1507, 1507), (1506, 1506), (1505, 1505), (1504, 1504), (1503, 1503), (1502, 1502), (1501, 1501), (1500, 1500), (1499, 1499), (1498, 1498), (1497, 1497), (1496, 1496), (1495, 1495), (1494, 1494), (1493, 1493), (1492, 1492), (1491, 1491), (1490, 1490), (1489, 1489), (1488, 1488), (1487, 1487), (1486, 1486), (1485, 1485), (1484, 1484), (1483, 1483), (1482, 1482), (1481, 1481), (1480, 1480), (1479, 1479), (1478, 1478), (1477, 1477), (1476, 1476), (1475, 1475), (1474, 1474), (1473, 1473), (1472, 1472), (1471, 1471), (1470, 1470), (1469, 1469), (1468, 1468), (1467, 1467), (1466, 1466), (1465, 1465), (1464, 1464), (1463, 1463), (1462, 1462), (1461, 1461), (1460, 1460), (1459, 1459), (1458, 1458), (1457, 1457), (1456, 1456), (1455, 1455), (1454, 1454), (1453, 1453), (1452, 1452), (1451, 1451), (1450, 1450), (1449, 1449), (1448, 1448), (1447, 1447), (1446, 1446), (1445, 1445), (1444, 1444), (1443, 1443), (1442, 1442), (1441, 1441), (1440, 1440), (1439, 1439), (1438, 1438), (1437, 1437), (1436, 1436), (1435, 1435), (1434, 1434), (1433, 1433), (1432, 1432), (1431, 1431), (1430, 1430), (1429, 1429), (1428, 1428), (1427, 1427), (1426, 1426), (1425, 1425), (1424, 1424), (1423, 1423), (1422, 1422), (1421, 1421), (1420, 1420), (1419, 1419), (1418, 1418), (1417, 1417), (1416, 1416), (1415, 1415), (1414, 1414), (1413, 1413), (1412, 1412), (1411, 1411), (1410, 1410), (1409, 1409), (1408, 1408), (1407, 1407), (1406, 1406), (1405, 1405), (1404, 1404), (1403, 1403), (1402, 1402), (1401, 1401), (1400, 1400), (1399, 1399), (1398, 1398), (1397, 1397), (1396, 1396), (1395, 1395), (1394, 1394), (1393, 1393), (1392, 1392), (1391, 1391), (1390, 1390), (1389, 1389), (1388, 1388), (1387, 1387), (1386, 1386), (1385, 1385), (1384, 1384), (1383, 1383), (1382, 1382), (1381, 1381), (1380, 1380), (1379, 1379), (1378, 1378), (1377, 1377), (1376, 1376), (1375, 1375), (1374, 1374), (1373, 1373), (1372, 1372), (1371, 1371), (1370, 1370), (1369, 1369), (1368, 1368), (1367, 1367), (1366, 1366), (1365, 1365), (1364, 1364), (1363, 1363), (1362, 1362), (1361, 1361), (1360, 1360), (1359, 1359), (1358, 1358), (1357, 1357), (1356, 1356), (1355, 1355), (1354, 1354), (1353, 1353), (1352, 1352), (1351, 1351), (1350, 1350), (1349, 1349), (1348, 1348), (1347, 1347), (1346, 1346), (1345, 1345), (1344, 1344), (1343, 1343), (1342, 1342), (1341, 1341), (1340, 1340), (1339, 1339), (1338, 1338), (1337, 1337), (1336, 1336), (1335, 1335), (1334, 1334), (1333, 1333), (1332, 1332), (1331, 1331), (1330, 1330), (1329, 1329), (1328, 1328), (1327, 1327), (1326, 1326), (1325, 1325), (1324, 1324), (1323, 1323), (1322, 1322), (1321, 1321), (1320, 1320), (1319, 1319), (1318, 1318), (1317, 1317), (1316, 1316), (1315, 1315), (1314, 1314), (1313, 1313), (1312, 1312), (1311, 1311), (1310, 1310), (1309, 1309), (1308, 1308), (1307, 1307), (1306, 1306), (1305, 1305), (1304, 1304), (1303, 1303), (1302, 1302), (1301, 1301), (1300, 1300), (1299, 1299), (1298, 1298), (1297, 1297), (1296, 1296), (1295, 1295), (1294, 1294), (1293, 1293), (1292, 1292), (1291, 1291), (1290, 1290), (1289, 1289), (1288, 1288), (1287, 1287), (1286, 1286), (1285, 1285), (1284, 1284), (1283, 1283), (1282, 1282), (1281, 1281), (1280, 1280), (1279, 1279), (1278, 1278), (1277, 1277), (1276, 1276), (1275, 1275), (1274, 1274), (1273, 1273), (1272, 1272), (1271, 1271), (1270, 1270), (1269, 1269), (1268, 1268), (1267, 1267), (1266, 1266), (1265, 1265), (1264, 1264), (1263, 1263), (1262, 1262), (1261, 1261), (1260, 1260), (1259, 1259), (1258, 1258), (1257, 1257), (1256, 1256), (1255, 1255), (1254, 1254), (1253, 1253), (1252, 1252), (1251, 1251), (1250, 1250), (1249, 1249), (1248, 1248), (1247, 1247), (1246, 1246), (1245, 1245), (1244, 1244), (1243, 1243), (1242, 1242), (1241, 1241), (1240, 1240), (1239, 1239), (1238, 1238), (1237, 1237), (1236, 1236), (1235, 1235), (1234, 1234), (1233, 1233), (1232, 1232), (1231, 1231), (1230, 1230), (1229, 1229), (1228, 1228), (1227, 1227), (1226, 1226), (1225, 1225), (1224, 1224), (1223, 1223), (1222, 1222), (1221, 1221), (1220, 1220), (1219, 1219), (1218, 1218), (1217, 1217), (1216, 1216), (1215, 1215), (1214, 1214), (1213, 1213), (1212, 1212), (1211, 1211), (1210, 1210), (1209, 1209), (1208, 1208), (1207, 1207), (1206, 1206), (1205, 1205), (1204, 1204), (1203, 1203), (1202, 1202), (1201, 1201), (1200, 1200), (1199, 1199), (1198, 1198), (1197, 1197), (1196, 1196), (1195, 1195), (1194, 1194), (1193, 1193), (1192, 1192), (1191, 1191), (1190, 1190), (1189, 1189), (1188, 1188), (1187, 1187), (1186, 1186), (1185, 1185), (1184, 1184), (1183, 1183), (1182, 1182), (1181, 1181), (1180, 1180), (1179, 1179), (1178, 1178), (1177, 1177), (1176, 1176), (1175, 1175), (1174, 1174), (1173, 1173), (1172, 1172), (1171, 1171), (1170, 1170), (1169, 1169), (1168, 1168), (1167, 1167), (1166, 1166), (1165, 1165), (1164, 1164), (1163, 1163), (1162, 1162), (1161, 1161), (1160, 1160), (1159, 1159), (1158, 1158), (1157, 1157), (1156, 1156), (1155, 1155), (1154, 1154), (1153, 1153), (1152, 1152), (1151, 1151), (1150, 1150), (1149, 1149), (1148, 1148), (1147, 1147), (1146, 1146), (1145, 1145), (1144, 1144), (1143, 1143), (1142, 1142), (1141, 1141), (1140, 1140), (1139, 1139), (1138, 1138), (1137, 1137), (1136, 1136), (1135, 1135), (1134, 1134), (1133, 1133), (1132, 1132), (1131, 1131), (1130, 1130), (1129, 1129), (1128, 1128), (1127, 1127), (1126, 1126), (1125, 1125), (1124, 1124), (1123, 1123), (1122, 1122), (1121, 1121), (1120, 1120), (1119, 1119), (1118, 1118), (1117, 1117), (1116, 1116), (1115, 1115), (1114, 1114), (1113, 1113), (1112, 1112), (1111, 1111), (1110, 1110), (1109, 1109), (1108, 1108), (1107, 1107), (1106, 1106), (1105, 1105), (1104, 1104), (1103, 1103), (1102, 1102), (1101, 1101), (1100, 1100), (1099, 1099), (1098, 1098), (1097, 1097), (1096, 1096), (1095, 1095), (1094, 1094), (1093, 1093), (1092, 1092), (1091, 1091), (1090, 1090), (1089, 1089), (1088, 1088), (1087, 1087), (1086, 1086), (1085, 1085), (1084, 1084), (1083, 1083), (1082, 1082), (1081, 1081), (1080, 1080), (1079, 1079), (1078, 1078), (1077, 1077), (1076, 1076), (1075, 1075), (1074, 1074), (1073, 1073), (1072, 1072), (1071, 1071), (1070, 1070), (1069, 1069), (1068, 1068), (1067, 1067), (1066, 1066), (1065, 1065), (1064, 1064), (1063, 1063), (1062, 1062), (1061, 1061), (1060, 1060), (1059, 1059), (1058, 1058), (1057, 1057), (1056, 1056), (1055, 1055), (1054, 1054), (1053, 1053), (1052, 1052), (1051, 1051), (1050, 1050), (1049, 1049), (1048, 1048), (1047, 1047), (1046, 1046), (1045, 1045), (1044, 1044), (1043, 1043), (1042, 1042), (1041, 1041), (1040, 1040), (1039, 1039), (1038, 1038), (1037, 1037), (1036, 1036), (1035, 1035), (1034, 1034), (1033, 1033), (1032, 1032), (1031, 1031), (1030, 1030), (1029, 1029), (1028, 1028), (1027, 1027), (1026, 1026), (1025, 1025), (1024, 1024), (1023, 1023), (1022, 1022), (1021, 1021), (1020, 1020), (1019, 1019), (1018, 1018), (1017, 1017), (1016, 1016), (1015, 1015), (1014, 1014), (1013, 1013), (1012, 1012), (1011, 1011), (1010, 1010), (1009, 1009), (1008, 1008), (1007, 1007), (1006, 1006), (1005, 1005), (1004, 1004), (1003, 1003), (1002, 1002), (1001, 1001), (1000, 1000), (999, 999), (998, 998), (997, 997), (996, 996), (995, 995), (994, 994), (993, 993), (992, 992), (991, 991), (990, 990), (989, 989), (988, 988), (987, 987), (986, 986), (985, 985), (984, 984), (983, 983), (982, 982), (981, 981), (980, 980), (979, 979), (978, 978), (977, 977), (976, 976), (975, 975), (974, 974), (973, 973), (972, 972), (971, 971), (970, 970), (969, 969), (968, 968), (967, 967), (966, 966), (965, 965), (964, 964), (963, 963), (962, 962), (961, 961), (960, 960), (959, 959), (958, 958), (957, 957), (956, 956), (955, 955), (954, 954), (953, 953), (952, 952), (951, 951), (950, 950), (949, 949), (948, 948), (947, 947), (946, 946), (945, 945), (944, 944), (943, 943), (942, 942), (941, 941), (940, 940), (939, 939), (938, 938), (937, 937), (936, 936), (935, 935), (934, 934), (933, 933), (932, 932), (931, 931), (930, 930), (929, 929), (928, 928), (927, 927), (926, 926), (925, 925), (924, 924), (923, 923), (922, 922), (921, 921), (920, 920), (919, 919), (918, 918), (917, 917), (916, 916), (915, 915), (914, 914), (913, 913), (912, 912), (911, 911), (910, 910), (909, 909), (908, 908), (907, 907), (906, 906), (905, 905), (904, 904), (903, 903), (902, 902), (901, 901), (900, 900), (899, 899), (898, 898), (897, 897), (896, 896), (895, 895), (894, 894), (893, 893), (892, 892), (891, 891), (890, 890), (889, 889), (888, 888), (887, 887), (886, 886), (885, 885), (884, 884), (883, 883), (882, 882), (881, 881), (880, 880), (879, 879), (878, 878), (877, 877), (876, 876), (875, 875), (874, 874), (873, 873), (872, 872), (871, 871), (870, 870), (869, 869), (868, 868), (867, 867), (866, 866), (865, 865), (864, 864), (863, 863), (862, 862), (861, 861), (860, 860), (859, 859), (858, 858), (857, 857), (856, 856), (855, 855), (854, 854), (853, 853), (852, 852), (851, 851), (850, 850), (849, 849), (848, 848), (847, 847), (846, 846), (845, 845), (844, 844), (843, 843), (842, 842), (841, 841), (840, 840), (839, 839), (838, 838), (837, 837), (836, 836), (835, 835), (834, 834), (833, 833), (832, 832), (831, 831), (830, 830), (829, 829), (828, 828), (827, 827), (826, 826), (825, 825), (824, 824), (823, 823), (822, 822), (821, 821), (820, 820), (819, 819), (818, 818), (817, 817), (816, 816), (815, 815), (814, 814), (813, 813), (812, 812), (811, 811), (810, 810), (809, 809), (808, 808), (807, 807), (806, 806), (805, 805), (804, 804), (803, 803), (802, 802), (801, 801), (800, 800), (799, 799), (798, 798), (797, 797), (796, 796), (795, 795), (794, 794), (793, 793), (792, 792), (791, 791), (790, 790), (789, 789), (788, 788), (787, 787), (786, 786), (785, 785), (784, 784), (783, 783), (782, 782), (781, 781), (780, 780), (779, 779), (778, 778), (777, 777), (776, 776), (775, 775), (774, 774), (773, 773), (772, 772), (771, 771), (770, 770), (769, 769), (768, 768), (767, 767), (766, 766), (765, 765), (764, 764), (763, 763), (762, 762), (761, 761), (760, 760), (759, 759), (758, 758), (757, 757), (756, 756), (755, 755), (754, 754), (753, 753), (752, 752), (751, 751), (750, 750), (749, 749), (748, 748), (747, 747), (746, 746), (745, 745), (744, 744), (743, 743), (742, 742), (741, 741), (740, 740), (739, 739), (738, 738), (737, 737), (736, 736), (735, 735), (734, 734), (733, 733), (732, 732), (731, 731), (730, 730), (729, 729), (728, 728), (727, 727), (726, 726), (725, 725), (724, 724), (723, 723), (722, 722), (721, 721), (720, 720), (719, 719), (718, 718), (717, 717), (716, 716), (715, 715), (714, 714), (713, 713), (712, 712), (711, 711), (710, 710), (709, 709), (708, 708), (707, 707), (706, 706), (705, 705), (704, 704), (703, 703), (702, 702), (701, 701), (700, 700), (699, 699), (698, 698), (697, 697), (696, 696), (695, 695), (694, 694), (693, 693), (692, 692), (691, 691), (690, 690), (689, 689), (688, 688), (687, 687), (686, 686), (685, 685), (684, 684), (683, 683), (682, 682), (681, 681), (680, 680), (679, 679), (678, 678), (677, 677), (676, 676), (675, 675), (674, 674), (673, 673), (672, 672), (671, 671), (670, 670), (669, 669), (668, 668), (667, 667), (666, 666), (665, 665), (664, 664), (663, 663), (662, 662), (661, 661), (660, 660), (659, 659), (658, 658), (657, 657), (656, 656), (655, 655), (654, 654), (653, 653), (652, 652), (651, 651), (650, 650), (649, 649), (648, 648), (647, 647), (646, 646), (645, 645), (644, 644), (643, 643), (642, 642), (641, 641), (640, 640), (639, 639), (638, 638), (637, 637), (636, 636), (635, 635), (634, 634), (633, 633), (632, 632), (631, 631), (630, 630), (629, 629), (628, 628), (627, 627), (626, 626), (625, 625), (624, 624), (623, 623), (622, 622), (621, 621), (620, 620), (619, 619), (618, 618), (617, 617), (616, 616), (615, 615), (614, 614), (613, 613), (612, 612), (611, 611), (610, 610), (609, 609), (608, 608), (607, 607), (606, 606), (605, 605), (604, 604), (603, 603), (602, 602), (601, 601), (600, 600), (599, 599), (598, 598), (597, 597), (596, 596), (595, 595), (594, 594), (593, 593), (592, 592), (591, 591), (590, 590), (589, 589), (588, 588), (587, 587), (586, 586), (585, 585), (584, 584), (583, 583), (582, 582), (581, 581), (580, 580), (579, 579), (578, 578), (577, 577), (576, 576), (575, 575), (574, 574), (573, 573), (572, 572), (571, 571), (570, 570), (569, 569), (568, 568), (567, 567), (566, 566), (565, 565), (564, 564), (563, 563), (562, 562), (561, 561), (560, 560), (559, 559), (558, 558), (557, 557), (556, 556), (555, 555), (554, 554), (553, 553), (552, 552), (551, 551), (550, 550), (549, 549), (548, 548), (547, 547), (546, 546), (545, 545), (544, 544), (543, 543), (542, 542), (541, 541), (540, 540), (539, 539), (538, 538), (537, 537), (536, 536), (535, 535), (534, 534), (533, 533), (532, 532), (531, 531), (530, 530), (529, 529), (528, 528), (527, 527), (526, 526), (525, 525), (524, 524), (523, 523), (522, 522), (521, 521), (520, 520), (519, 519), (518, 518), (517, 517), (516, 516), (515, 515), (514, 514), (513, 513), (512, 512), (511, 511), (510, 510), (509, 509), (508, 508), (507, 507), (506, 506), (505, 505), (504, 504), (503, 503), (502, 502), (501, 501), (500, 500), (499, 499), (498, 498), (497, 497), (496, 496), (495, 495), (494, 494), (493, 493), (492, 492), (491, 491), (490, 490), (489, 489), (488, 488), (487, 487), (486, 486), (485, 485), (484, 484), (483, 483), (482, 482), (481, 481), (480, 480), (479, 479), (478, 478), (477, 477), (476, 476), (475, 475), (474, 474), (473, 473), (472, 472), (471, 471), (470, 470), (469, 469), (468, 468), (467, 467), (466, 466), (465, 465), (464, 464), (463, 463), (462, 462), (461, 461), (460, 460), (459, 459), (458, 458), (457, 457), (456, 456), (455, 455), (454, 454), (453, 453), (452, 452), (451, 451), (450, 450), (449, 449), (448, 448), (447, 447), (446, 446), (445, 445), (444, 444), (443, 443), (442, 442), (441, 441), (440, 440), (439, 439), (438, 438), (437, 437), (436, 436), (435, 435), (434, 434), (433, 433), (432, 432), (431, 431), (430, 430), (429, 429), (428, 428), (427, 427), (426, 426), (425, 425), (424, 424), (423, 423), (422, 422), (421, 421), (420, 420), (419, 419), (418, 418), (417, 417), (416, 416), (415, 415), (414, 414), (413, 413), (412, 412), (411, 411), (410, 410), (409, 409), (408, 408), (407, 407), (406, 406), (405, 405), (404, 404), (403, 403), (402, 402), (401, 401), (400, 400), (399, 399), (398, 398), (397, 397), (396, 396), (395, 395), (394, 394), (393, 393), (392, 392), (391, 391), (390, 390), (389, 389), (388, 388), (387, 387), (386, 386), (385, 385), (384, 384), (383, 383), (382, 382), (381, 381), (380, 380), (379, 379), (378, 378), (377, 377), (376, 376), (375, 375), (374, 374), (373, 373), (372, 372), (371, 371), (370, 370), (369, 369), (368, 368), (367, 367), (366, 366), (365, 365), (364, 364), (363, 363), (362, 362), (361, 361), (360, 360), (359, 359), (358, 358), (357, 357), (356, 356), (355, 355), (354, 354), (353, 353), (352, 352), (351, 351), (350, 350), (349, 349), (348, 348), (347, 347), (346, 346), (345, 345), (344, 344), (343, 343), (342, 342), (341, 341), (340, 340), (339, 339), (338, 338), (337, 337), (336, 336), (335, 335), (334, 334), (333, 333), (332, 332), (331, 331), (330, 330), (329, 329), (328, 328), (327, 327), (326, 326), (325, 325), (324, 324), (323, 323), (322, 322), (321, 321), (320, 320), (319, 319), (318, 318), (317, 317), (316, 316), (315, 315), (314, 314), (313, 313), (312, 312), (311, 311), (310, 310), (309, 309), (308, 308), (307, 307), (306, 306), (305, 305), (304, 304), (303, 303), (302, 302), (301, 301), (300, 300), (299, 299), (298, 298), (297, 297), (296, 296), (295, 295), (294, 294), (293, 293), (292, 292), (291, 291), (290, 290), (289, 289), (288, 288), (287, 287), (286, 286), (285, 285), (284, 284), (283, 283), (282, 282), (281, 281), (280, 280), (279, 279), (278, 278), (277, 277), (276, 276), (275, 275), (274, 274), (273, 273), (272, 272), (271, 271), (270, 270), (269, 269), (268, 268), (267, 267), (266, 266), (265, 265), (264, 264), (263, 263), (262, 262), (261, 261), (260, 260), (259, 259), (258, 258), (257, 257), (256, 256), (255, 255), (254, 254), (253, 253), (252, 252), (251, 251), (250, 250), (249, 249), (248, 248), (247, 247), (246, 246), (245, 245), (244, 244), (243, 243), (242, 242), (241, 241), (240, 240), (239, 239), (238, 238), (237, 237), (236, 236), (235, 235), (234, 234), (233, 233), (232, 232), (231, 231), (230, 230), (229, 229), (228, 228), (227, 227), (226, 226), (225, 225), (224, 224), (223, 223), (222, 222), (221, 221), (220, 220), (219, 219), (218, 218), (217, 217), (216, 216), (215, 215), (214, 214), (213, 213), (212, 212), (211, 211), (210, 210), (209, 209), (208, 208), (207, 207), (206, 206), (205, 205), (204, 204), (203, 203), (202, 202), (201, 201), (200, 200), (199, 199), (198, 198), (197, 197), (196, 196), (195, 195), (194, 194), (193, 193), (192, 192), (191, 191), (190, 190), (189, 189), (188, 188), (187, 187), (186, 186), (185, 185), (184, 184), (183, 183), (182, 182), (181, 181), (180, 180), (179, 179), (178, 178), (177, 177), (176, 176), (175, 175), (174, 174), (173, 173), (172, 172), (171, 171), (170, 170), (169, 169), (168, 168), (167, 167), (166, 166), (165, 165), (164, 164), (163, 163), (162, 162), (161, 161), (160, 160), (159, 159), (158, 158), (157, 157), (156, 156), (155, 155), (154, 154), (153, 153), (152, 152), (151, 151), (150, 150), (149, 149), (148, 148), (147, 147), (146, 146), (145, 145), (144, 144), (143, 143), (142, 142), (141, 141), (140, 140), (139, 139), (138, 138), (137, 137), (136, 136), (135, 135), (134, 134), (133, 133), (132, 132), (131, 131), (130, 130), (129, 129), (128, 128), (127, 127), (126, 126), (125, 125), (124, 124), (123, 123), (122, 122), (121, 121), (120, 120), (119, 119), (118, 118), (117, 117), (116, 116), (115, 115), (114, 114), (113, 113), (112, 112), (111, 111), (110, 110), (109, 109), (108, 108), (107, 107), (106, 106), (105, 105), (104, 104), (103, 103), (102, 102), (101, 101), (100, 100), (99, 99), (98, 98), (97, 97), (96, 96), (95, 95), (94, 94), (93, 93), (92, 92), (91, 91), (90, 90), (89, 89), (88, 88), (87, 87), (86, 86), (85, 85), (84, 84), (83, 83), (82, 82), (81, 81), (80, 80), (79, 79), (78, 78), (77, 77), (76, 76), (75, 75), (74, 74), (73, 73), (72, 72), (71, 71), (70, 70), (69, 69), (68, 68), (67, 67), (66, 66), (65, 65), (64, 64), (63, 63), (62, 62), (61, 61), (60, 60), (59, 59), (58, 58), (57, 57), (56, 56), (55, 55), (54, 54), (53, 53), (52, 52), (51, 51), (50, 50), (49, 49), (48, 48), (47, 47), (46, 46), (45, 45), (44, 44), (43, 43), (42, 42), (41, 41), (40, 40), (39, 39), (38, 38), (37, 37), (36, 36), (35, 35), (34, 34), (33, 33), (32, 32), (31, 31), (30, 30), (29, 29), (28, 28), (27, 27), (26, 26), (25, 25), (24, 24), (23, 23), (22, 22), (21, 21), (20, 20), (19, 19), (18, 18), (17, 17), (16, 16), (15, 15), (14, 14), (13, 13), (12, 12), (11, 11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=2016)),
                ('status', models.CharField(choices=[('available', 'Available'), ('checked out', 'Checked Out')], default='available', max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_borrowed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]