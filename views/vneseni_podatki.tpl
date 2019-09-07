% rebase('osnovna_stran.tpl')

<p>
    <br><i>Začetek prejšnjega cikla:</i> <b>{{datum_vnos}}</b>
    <br><i>Dolžina cikla:</i> <b>{{dolzina_vnos}} dni</b>
    % if trajanje_vnos == 1:
        <br><i>Trajanje menstruacije:</i> <b>{{trajanje_vnos}} dan</b>
    % elif trajanje_vnos == 2:
        <br><i>Trajanje menstruacije:</i> <b>{{trajanje_vnos}} dneva</b>
    % else:
        <br><i>Trajanje menstruacije:</i> <b>{{trajanje_vnos}} dni</b>
    % end
    <br> {{!base}}
</p>