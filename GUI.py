<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.20.0 -->
<interface>
  <requires lib="gtk+" version="3.0"/>
  <object class="GtkWindow">
    <property name="can_focus">False</property>
    <child>
      <object class="GtkNotebook">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="tab_pos">left</property>
        <child>
          <object class="GtkBox">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="orientation">vertical</property>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
            <child>
              <placeholder/>
            </child>
          </object>
        </child>
        <child type="tab">
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">GPU</property>
          </object>
          <packing>
            <property name="tab_fill">False</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">not avaliable</property>
          </object>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
        <child type="tab">
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">Wifi</property>
          </object>
          <packing>
            <property name="position">1</property>
            <property name="tab_fill">False</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">lNot Avlaible</property>
          </object>
          <packing>
            <property name="position">2</property>
          </packing>
        </child>
        <child type="tab">
          <object class="GtkLabel">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="label" translatable="yes">Kernel</property>
          </object>
          <packing>
            <property name="position">2</property>
            <property name="tab_fill">False</property>
          </packing>
        </child>
      </object>
    </child>
    <child>
      <placeholder/>
    </child>
  </object>
</interface>