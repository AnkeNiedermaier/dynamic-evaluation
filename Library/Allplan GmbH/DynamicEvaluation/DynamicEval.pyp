<?xml version="1.0" encoding="utf-8"?>
<Element xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPart.xsd">
    <Script>
        <Name>allplan_gmbh\DynamicEvaluation\DynamicEval.py</Name>
        <TextId>1000</TextId>
        <Title>Dynamic Evaluation</Title>
        <Version>1.0</Version>
        <Interactor>False</Interactor>
        <ReadLastInput>False</ReadLastInput>
    </Script>
    <Page>
        <Name>Page1</Name>
        <TextId>1001</TextId>
        <Text>Settings</Text>
        <Parameters>
            <Parameter>
                <Name>Image</Name>
                <Value>DynamicEval.svg</Value>
                <Orientation>Middle</Orientation>
                <ValueType>Picture</ValueType>
            </Parameter>

<!-- Evaluation start -->
            <Parameter>
                <Name>Expander</Name>
                <TextId>1005</TextId>
                <Text>Evaluation</Text>
                <ValueType>Expander</ValueType>
                <Value>False</Value>
                <Parameters>
                    <Parameter>
                        <Name>Row109</Name>
                        <TextId>1006</TextId>
                        <Text>Evaluation window</Text>
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
