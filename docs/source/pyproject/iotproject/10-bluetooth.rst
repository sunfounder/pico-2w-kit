.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Vertiefen Sie Ihr Wissen über Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und Einblicke.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

8.10 Einstieg in Bluetooth
=================================

Der Raspberry Pi Pico 2 W verfügt über ein Infineon CYW43439 Modem, das 2.4GHz 802.11n Wi-Fi und Bluetooth 5.2 Konnektivität bietet. In MicroPython wird derzeit nur Bluetooth Low Energy (BLE) unterstützt; klassisches Bluetooth ist nicht verfügbar.

Mehrere BLE-Beispiele werden bereitgestellt, um Ihnen den Einstieg in die Entwicklung von Bluetooth-Projekten zu erleichtern. Bevor Sie beginnen, lesen Sie den folgenden Artikel, um sich mit den grundlegenden Konzepten von BLE vertraut zu machen.

Grundkonzepte von Bluetooth Low Energy
++++++++++++++++++++++++++++++++++++++++++++++++

**Bluetooth Low Energy (BLE)** ist eine energiesparende drahtlose Kommunikationstechnologie, die speziell für Kurzstreckeninteraktionen entwickelt wurde. Im Gegensatz zum klassischen Bluetooth konzentriert sich BLE auf Energieeffizienz und schnelle Verbindung, was es zu einer idealen Wahl für eine Vielzahl von Anwendungen macht, einschließlich Internet der Dinge (IoT)-Geräte und Gesundheitsüberwachungsausrüstung.

BLE-Kommunikationen stützen sich auf zwei Schlüsselprotokolle: **Generic Attribute Profile (GATT)** und **Generic Access Profile (GAP)**. GATT wird für den Datenaustausch verwendet, während GAP für die Geräteerkennung und Verbindung verantwortlich ist.

.. image:: img/ble.png
 :width: 100%


Peripheriegeräte (typischerweise GATT-Server)
--------------------------------------------------

In einem BLE-Netzwerk senden **Peripheriegeräte** hauptsächlich Daten, um von zentralen Geräten (typischerweise als GATT-Clients agierend) entdeckt und zugegriffen zu werden. Solche Geräte sind in der Regel Sensoren oder kleine Hardware wie Herzfrequenzmonitore, Temperatursensoren oder intelligente Glühbirnen.

Im BLE-Kommunikationsmodell bieten Peripheriegeräte oft eine oder mehrere **Dienste**, die jeweils eine Reihe von **Eigenschaften** enthalten. Diese Dienste und Eigenschaften ermöglichen gemeinsam spezifische Funktionalitäten oder Anwendungsfälle, die es zentralen Geräten erlauben, relevante Daten zu lesen oder zu manipulieren.

- **Dienste**

  In BLE fungieren Dienste als hochrangige Abstraktionen, die verwendet werden, um verwandte Eigenschaften zu organisieren und zu kapseln. Dienste in BLE können je nach Herkunft und Zweck in Standarddienste und benutzerdefinierte Dienste unterteilt werden.

  - Standarddienste: Vom Bluetooth SIG (Bluetooth Special Interest Group) definiert, dienen diese spezifischen Funktionen. Zum Beispiel der Herzfrequenzdienst für Herzfrequenzmonitore, der Geräteinformationsdienst, der Hersteller-, Modell- und Versionsdetails bereitstellt, und der Batteriedienst, der Batterieniveau und -status angibt. Referenz: |link_standard_service_uuids| 
  - Benutzerdefinierte Dienste: Diese werden von Entwicklern oder Geräteherstellern definiert, um den Anforderungen spezifischer Anwendungen oder Geräte gerecht zu werden. Beispielsweise könnte ein Hersteller von Smart-Home-Geräten einen benutzerdefinierten Dienst definieren, um die Lichtfarbe und -helligkeit zu steuern.

- **Eigenschaften**

  Eigenschaften in BLE sind die grundlegenden Dateneinheiten, die von Peripheriegeräten bereitgestellt werden. Sie sind in einem Dienst enthalten und definieren verschiedene Datentypen sowie die Operationen, die an ihnen durchgeführt werden können. Jede Eigenschaft wird durch eine UUID identifiziert und hat eine Reihe von zugehörigen Attributen wie Wert, Beschreibung und Berechtigungen.

  - Berechtigungen: In BLE wird jeder Eigenschaft ein Satz von Berechtigungen zugeordnet, der festlegt, ob die Eigenschaft lesbar, beschreibbar oder benachrichtigbar ist. Dies hilft dabei, die Daten zu sichern und zu definieren, wie damit interagiert wird.

- **UUID**

  Dienste, Eigenschaften und Beschreibungen werden kollektiv als Attribute identifiziert, jedes mit einer einzigartigen UUID. Die Bluetooth SIG hat eine Reihe von UUIDs für Standardattribute reserviert. Diese UUIDs werden im BLE-Protokoll normalerweise als 16-Bit- oder 32-Bit-Identifikatoren dargestellt, anstatt der 128 Bits, die für eine vollständige UUID erforderlich sind. Beispielsweise wird der Geräteinformationsservice durch den Kurzcode 0x180A dargestellt.



Zentralgeräte (typischerweise GATT-Clients)
--------------------------------------------------

**Zentralgeräte** im BLE-Netzwerk scannen nach nahen Peripheriegeräten und stellen Verbindungen her, um Daten zu erwerben oder zu steuern. Diese Geräte sind in der Regel komplexer und funktionsreicher, wie Smartphones, Tablets oder spezialisierte Gateway-Hardware. Sie sind verantwortlich für die Entdeckung von Peripheriegeräten, deren Verbindung und den Zugriff oder das Abonnieren von Diensten und Eigenschaften, die von den Peripheriegeräten angeboten werden, um verschiedene Anwendungen zu bedienen oder spezifische Probleme zu lösen.

Zentralgeräte interagieren auf folgende Weise mit Eigenschaften:

- **Lesen**: Fordern Sie das Peripheriegerät auf, den aktuellen Wert einer Eigenschaft zu senden. Dies wird häufig für Eigenschaften verwendet, die sich nicht oft ändern, wie Konfigurationseinstellungen oder Versionsnummern.
- **Schreiben**: Ändern Sie den Wert einer Eigenschaft, typischerweise verwendet für Befehlsoperationen, wie das Anweisen eines Peripheriegeräts, einen Motor ein- oder auszuschalten.
- **Abonnieren**: Fordern Sie das Peripheriegerät auf, kontinuierlich aktualisierte Werte einer Eigenschaft zu senden, wodurch die Notwendigkeit für das Zentralgerät entfällt, diese Daten wiederholt anzufordern.
