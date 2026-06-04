<?xml version="1.0" encoding="utf-8"?>
<Element xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPart.xsd">
    <Script>
        <Name>allplan_gmbh\DynamicEval.py</Name>
        <Title>Dynamic Evaluation</Title>
        <Version>1.0</Version>
        <Interactor>False</Interactor>
        <ReadLastInput>False</ReadLastInput>
    </Script>
    <Page>
        <Name>Page1</Name>
        <Text>Einstellungen</Text>
        <Parameters>
            <Parameter>
                <Name>Image</Name>
                <Value>DynamicEval.svg</Value>
                <Orientation>Middle</Orientation>
                <ValueType>Picture</ValueType>
            </Parameter>
<!-- Attribute selection -->
            <Parameter>
                <Name>Expander</Name>
                <TextId>1001</TextId>
                <Text>Eval file path</Text>
                <ValueType>Expander</ValueType>
                <Value>False</Value>
                <Parameters>
                    <Parameter>
                        <Name>Row1</Name>
                        <TextId>1009</TextId>
                        <Text>Path selection</Text>
                        <ValueType>Row</ValueType>
                        <Parameters>
                            <Parameter>
                                <Name>eval_file_path</Name>
                                <TextId>1010</TextId>
                                <Text>select</Text>
                                <Value></Value>
                                <ValueType>String</ValueType>
                                <ValueDialog>OpenFileDialog</ValueDialog>
                                <FileFilter>Text file(*.txt)|*.txt|</FileFilter>
                                <FileExtension>txt</FileExtension>
                                <DefaultDirectories>std|prj</DefaultDirectories>
                            </Parameter>
                        </Parameters>
                    </Parameter>
                </Parameters>
            </Parameter>
<!-- Evaluation start -->
            <Parameter>
                <Name>Expander</Name>
                <TextId>1006</TextId>
                <Text>Evaluation</Text>
                <ValueType>Expander</ValueType>
                <Value>False</Value>
                <Parameters>
                    <Parameter>
                        <Name>Row109</Name>
                        <TextId>1006</TextId>
                        <Text>Diagram</Text>
                        <ValueType>Row</ValueType>
                        <Parameters>
                            <Parameter>
                                <Name>start_eval</Name>
                                <TextId>1007</TextId>
                                <Text>start</Text>
                                <EventId>1000</EventId>
                                <ValueType>Button</ValueType>
                            </Parameter>
                        </Parameters>
                    </Parameter>
                </Parameters>
            </Parameter>
        </Parameters>
    </Page>
</Element>
