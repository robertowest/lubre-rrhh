# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# python3 manage.py inspectdb --database=mysql --include-views > inspectdb.txt
#
from django.db import models


class Actividades(models.Model):
    idactividad = models.IntegerField(primary_key=True)
    idcanales = models.ForeignKey('Canales', models.DO_NOTHING, db_column='idcanales')
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    secretaria = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades'


class Alicuotasprov(models.Model):
    idalicuotasprov = models.IntegerField(primary_key=True)
    idfacprovedor = models.ForeignKey('Facprovedor', models.DO_NOTHING, db_column='idfacprovedor')
    idalicuota = models.IntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    impalicuota = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    importe1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    importe2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alicuotasprov'


class Anula(models.Model):
    idenc_mov = models.IntegerField()
    idtipo_comp = models.CharField(max_length=10, blank=True, null=True)
    concepto = models.CharField(max_length=80, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fechaanula = models.DateField(blank=True, null=True)
    operaanula = models.IntegerField(blank=True, null=True)
    idoperacaja = models.IntegerField(blank=True, null=True)
    tipoopera = models.SmallIntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anula'


class Asientos(models.Model):
    idasiento = models.IntegerField(primary_key=True)
    idtipfon = models.ForeignKey('Tipfon', models.DO_NOTHING, db_column='idtipfon')
    idenc_mov = models.ForeignKey('EncMov', models.DO_NOTHING, db_column='idenc_mov')
    idplan = models.ForeignKey('Plancta', models.DO_NOTHING, db_column='idplan')
    iddet_centro = models.ForeignKey('DetCentro', models.DO_NOTHING, db_column='iddet_centro', blank=True, null=True)
    idpers_subcta = models.ForeignKey('PersSubcta', models.DO_NOTHING, db_column='idpers_subcta', blank=True, null=True)
    detalle = models.CharField(max_length=80, blank=True, null=True)
    cotizacion = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    percrec = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    recargo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    tipsub = models.CharField(max_length=1, blank=True, null=True)
    codsub = models.IntegerField(blank=True, null=True)
    subcuenta = models.IntegerField(blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.SmallIntegerField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    planilla = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asientos'


class Asientostmp(models.Model):
    idasiento = models.IntegerField(primary_key=True)
    idtipfon = models.IntegerField()
    idenc_mov = models.IntegerField()
    idplan = models.IntegerField()
    iddet_centro = models.IntegerField(blank=True, null=True)
    idpers_subcta = models.IntegerField(blank=True, null=True)
    detalle = models.CharField(max_length=50, blank=True, null=True)
    cotizacion = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    percrec = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    recargo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tipsub = models.CharField(max_length=1, blank=True, null=True)
    codsub = models.IntegerField(blank=True, null=True)
    subcuenta = models.IntegerField(blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.SmallIntegerField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    planilla = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asientostmp'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.SmallIntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Autoriza(models.Model):
    idautoriza = models.IntegerField(primary_key=True)
    idusuario = models.IntegerField(blank=True, null=True)
    rutina = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autoriza'


class Bancos(models.Model):
    idbanco = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'


class Cajadiaria(models.Model):
    idcajadiaria = models.IntegerField(primary_key=True)
    apertura = models.DateField(blank=True, null=True)
    cierre = models.DateField(blank=True, null=True)
    idusuario = models.ForeignKey('TUsuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'cajadiaria'


class Califica(models.Model):
    idcalifica = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'califica'


class Campos(models.Model):
    nombrecolumna = models.CharField(max_length=50, blank=True, null=True)
    nombrecampo = models.CharField(max_length=100, blank=True, null=True)
    orden = models.CharField(max_length=50, blank=True, null=True)
    ordencampos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campos'


class Canales(models.Model):
    idcanales = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canales'


class Cartera(models.Model):
    idcartera = models.IntegerField(primary_key=True)
    idasiento = models.ForeignKey(Asientos, models.DO_NOTHING, db_column='idasiento')
    vence = models.DateField(blank=True, null=True)
    banco = models.CharField(max_length=50, blank=True, null=True)
    cuenta = models.CharField(max_length=10, blank=True, null=True)
    numero_fon = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    orden = models.CharField(max_length=50, blank=True, null=True)
    concilia = models.DateField(blank=True, null=True)
    fechareal = models.DateField(blank=True, null=True)
    hoja = models.IntegerField(blank=True, null=True)
    idcliente = models.IntegerField(blank=True, null=True)
    idproveedor = models.IntegerField(blank=True, null=True)
    cuotas = models.SmallIntegerField(blank=True, null=True)
    ingreso = models.CharField(max_length=20, blank=True, null=True)
    salidfondo = models.IntegerField(blank=True, null=True)
    recargo = models.IntegerField(blank=True, null=True)
    percrec = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    salidaasi = models.IntegerField(blank=True, null=True)
    idresumen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartera'


class Categoriascliente(models.Model):
    idcategoriacliente = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'categoriascliente'


class Centro(models.Model):
    idcentro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centro'


class CliNivel1(models.Model):
    idcli_nivel1 = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cli_nivel1'


class CliNivel2(models.Model):
    idcli_nivel2 = models.IntegerField(primary_key=True)
    idcli_nivel1 = models.ForeignKey(CliNivel1, models.DO_NOTHING, db_column='idcli_nivel1', blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cli_nivel2'


class CliNivel3(models.Model):
    idcli_nivel3 = models.IntegerField(primary_key=True)
    idcli_nivel2 = models.ForeignKey(CliNivel2, models.DO_NOTHING, db_column='idcli_nivel2', blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cli_nivel3'


class Clictas(models.Model):
    idclicta = models.IntegerField(primary_key=True)
    idplan = models.IntegerField(blank=True, null=True)
    idcliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='idcliente')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clictas'


class Clientecla(models.Model):
    idclientecla = models.IntegerField(primary_key=True)
    item = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientecla'


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    idactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    idcalifica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    idestadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='idestadocliente')
    idformacobro = models.ForeignKey('Formacobros', models.DO_NOTHING, db_column='idformacobro')
    idtipoingbruto = models.ForeignKey('Tipoingbruto', models.DO_NOTHING, db_column='idtipoingbruto')
    idlista = models.ForeignKey('Listas', models.DO_NOTHING, db_column='idlista')
    idtipimun = models.ForeignKey('Tipimun', models.DO_NOTHING, db_column='idtipimun')
    idtipoiva = models.ForeignKey('Tipoiva', models.DO_NOTHING, db_column='idtipoiva')
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    padron = models.CharField(max_length=10, blank=True, null=True)
    canal = models.IntegerField(blank=True, null=True)
    tipoope = models.CharField(max_length=1, blank=True, null=True)
    credito = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    maxsant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    morapant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ctacte = models.IntegerField(blank=True, null=True)
    directivos = models.CharField(max_length=60, blank=True, null=True)
    direc_d = models.CharField(max_length=60, blank=True, null=True)
    telef_d = models.CharField(max_length=20, blank=True, null=True)
    email_d = models.CharField(max_length=90, blank=True, null=True)
    codpro1 = models.CharField(max_length=15, blank=True, null=True)
    comision = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)
    idplancanje = models.IntegerField(blank=True, null=True)
    bloqueado = models.CharField(max_length=1, blank=True, null=True)
    idclasifica = models.IntegerField(blank=True, null=True)
    fechacalifica = models.DateField(blank=True, null=True)
    idcli_nivel1 = models.IntegerField(blank=True, null=True)
    idcli_nivel2 = models.IntegerField(blank=True, null=True)
    idcli_nivel3 = models.IntegerField(blank=True, null=True)
    idprocanje = models.IntegerField(blank=True, null=True)
    idprovincias = models.CharField(max_length=15, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    idtipodoc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Clientessucursal(models.Model):
    idclientesucursal = models.IntegerField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idvendedor')
    idvendedor2 = models.IntegerField(blank=True, null=True)
    idprovincias = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idprovincias')
    sucursal = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    codpos = models.CharField(max_length=12, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=90, blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    flete = models.IntegerField(blank=True, null=True)
    indcomis = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    reparto = models.IntegerField(blank=True, null=True)
    entrega = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    km = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    departamento = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientessucursal'


class Codajuste(models.Model):
    idcodajuste = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    abrevia = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    familia = models.CharField(max_length=1, blank=True, null=True)
    devolucion = models.CharField(max_length=1, blank=True, null=True)
    stock = models.CharField(max_length=1, blank=True, null=True)
    cheques = models.CharField(max_length=1, blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)
    idplan1 = models.IntegerField(blank=True, null=True)
    anulacomp = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codajuste'


class Codigobarra(models.Model):
    idcodigobarra = models.IntegerField(primary_key=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    formula = models.BinaryField(blank=True, null=True)
    idtipfon = models.ForeignKey('Tipfon', models.DO_NOTHING, db_column='idtipfon')
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cadenacontrol = models.CharField(max_length=100, blank=True, null=True)
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigobarra'


class Colegio(models.Model):
    idcolegio = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    abrevia = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    linea1 = models.CharField(max_length=80, blank=True, null=True)
    linea2 = models.CharField(max_length=80, blank=True, null=True)
    linea3 = models.CharField(max_length=40, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    encrecibo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colegio'


class ComprobConta(models.Model):
    idcomprobante = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    tipocomprob = models.CharField(max_length=3, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    puntoventa = models.SmallIntegerField(blank=True, null=True)
    numero = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    cai = models.CharField(max_length=20, blank=True, null=True)
    vencimiento = models.DateField(blank=True, null=True)
    tipo_opera = models.CharField(max_length=20, blank=True, null=True)
    pago_cobro = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=50, blank=True, null=True)
    provedor = models.CharField(max_length=1, blank=True, null=True)
    aplicable = models.CharField(max_length=1, blank=True, null=True)
    cliente = models.CharField(max_length=1, blank=True, null=True)
    empleado = models.CharField(max_length=1, blank=True, null=True)
    propio = models.CharField(max_length=1, blank=True, null=True)
    tercero = models.CharField(max_length=1, blank=True, null=True)
    signo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprob_conta'


class Comprobdev(models.Model):
    devenga = models.IntegerField(blank=True, null=True)
    idalumno = models.IntegerField(blank=True, null=True)
    nrocomprob = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comprobdev'


class ControldeudaAccion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    tipo = models.SmallIntegerField()
    texto = models.TextField()
    factura = models.ForeignKey('ControldeudaFactura', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'controldeuda_accion'


class ControldeudaCliente(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    referencia_id = models.IntegerField(unique=True)
    comercial = models.ForeignKey('ControldeudaComercial', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'controldeuda_cliente'


class ControldeudaComercial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'controldeuda_comercial'


class ControldeudaFactura(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    tipo = models.CharField(max_length=3)
    tipo_letra = models.CharField(max_length=1)
    sucursal = models.IntegerField()
    numero = models.IntegerField()
    producto = models.CharField(max_length=60)
    total = models.FloatField()
    vencimiento = models.DateField()
    cliente = models.ForeignKey(ControldeudaCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'controldeuda_factura'


class Ctaprovedor(models.Model):
    idctaprovedor = models.IntegerField(primary_key=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_f = models.DateField(blank=True, null=True)
    moneda = models.CharField(max_length=1, blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    ref_comp = models.CharField(max_length=15, blank=True, null=True)
    ref_let = models.CharField(max_length=1, blank=True, null=True)
    ref_ter = models.IntegerField(blank=True, null=True)
    ref_num = models.IntegerField(blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)
    cuota = models.IntegerField(blank=True, null=True)
    cuotas = models.IntegerField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    motivo = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=60, blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    relacion = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    formap = models.IntegerField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctaprovedor'


class Cuentacte(models.Model):
    idcuentacte = models.IntegerField(primary_key=True)
    sucursal = models.IntegerField(blank=True, null=True)
    idcliente = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    cuota = models.IntegerField(blank=True, null=True)
    cuotas = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ref_comp = models.CharField(max_length=15, blank=True, null=True)
    ref_let = models.CharField(max_length=1, blank=True, null=True)
    ref_ter = models.IntegerField(blank=True, null=True)
    ref_num = models.IntegerField(blank=True, null=True)
    ref_cuo = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=120, blank=True, null=True)
    conmay = models.IntegerField(blank=True, null=True)
    ocarga = models.IntegerField(blank=True, null=True)
    idtransporte = models.IntegerField(blank=True, null=True)
    rinde = models.IntegerField(blank=True, null=True)
    recibom = models.IntegerField(blank=True, null=True)
    fecham = models.DateField(blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentacte'


class Departamentos(models.Model):
    iddepartamento = models.CharField(primary_key=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Depos(models.Model):
    iddepos = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    abrevia = models.CharField(max_length=40, blank=True, null=True)
    fisico = models.CharField(max_length=1, blank=True, null=True)
    suma = models.CharField(max_length=1, blank=True, null=True)
    autoriza = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    provincia = models.CharField(max_length=1, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    emal = models.CharField(max_length=120, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'depos'


class DetCentro(models.Model):
    iddet_centro = models.IntegerField(primary_key=True)
    idcentro = models.ForeignKey(Centro, models.DO_NOTHING, db_column='idcentro')
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    datos = models.CharField(max_length=80, blank=True, null=True)
    porcent = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_centro'


class DetModelo(models.Model):
    iddet_modelo = models.IntegerField(primary_key=True)
    detalle = models.CharField(max_length=50, blank=True, null=True)
    idmodeloasi = models.ForeignKey('Modeloasi', models.DO_NOTHING, db_column='idmodeloasi')
    idplan = models.IntegerField()
    idtipfon = models.IntegerField(blank=True, null=True)
    iddet_centro = models.IntegerField(blank=True, null=True)
    idpers_subcta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'det_modelo'


class Detcomision(models.Model):
    iddetcomision = models.IntegerField(primary_key=True)
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idvendedor')
    comisioncobro = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    diascobro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detcomision'


class Detformacobro(models.Model):
    iddetformacobro = models.IntegerField(primary_key=True)
    idformacobro = models.ForeignKey('Formacobros', models.DO_NOTHING, db_column='idformacobro')
    cuota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detformacobro'


class Detformapago(models.Model):
    iddetformapago = models.IntegerField(primary_key=True)
    idformapago = models.ForeignKey('Formapagos', models.DO_NOTHING, db_column='idformapago')
    cuota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detformapago'


class Detstock(models.Model):
    iddetstock = models.IntegerField(primary_key=True)
    stock_idstock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='stock_idstock')
    lote = models.IntegerField(blank=True, null=True)
    dato1 = models.CharField(max_length=30, blank=True, null=True)
    dato2 = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    inicial = models.DateField(blank=True, null=True)
    final = models.DateField(blank=True, null=True)
    iddepos = models.ForeignKey(Depos, models.DO_NOTHING, db_column='iddepos')
    stock = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    sstock = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detstock'


class Division(models.Model):
    iddivision = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'division'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctipos(models.Model):
    iddoctipo = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'doctipos'


class Ejercicios(models.Model):
    idejercicio = models.IntegerField(primary_key=True)
    ejercicio = models.CharField(max_length=30, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    fechainicio = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejercicios'


class EncMov(models.Model):
    idenc_mov = models.IntegerField(primary_key=True)
    idtipo_comp = models.CharField(max_length=10, blank=True, null=True)
    idejercicio = models.ForeignKey(Ejercicios, models.DO_NOTHING, db_column='idejercicio')
    concepto = models.CharField(max_length=80, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)
    tipo_opera = models.CharField(max_length=20, blank=True, null=True)
    idoperacaja = models.IntegerField(blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_mov'


class Estadocliente(models.Model):
    idestadocliente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocliente'


class Facprovedor(models.Model):
    idfacprovedor = models.IntegerField(primary_key=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    idenc_mov = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_f = models.DateField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    cierre = models.DateField(blank=True, null=True)
    neto = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    ibruto = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    formap = models.IntegerField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=80, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    nograv = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    tipo_fac = models.CharField(max_length=15, blank=True, null=True)
    numero_fac = models.IntegerField(blank=True, null=True)
    letra_fac = models.CharField(max_length=1, blank=True, null=True)
    terminal_fac = models.IntegerField(blank=True, null=True)
    idprovedortmp = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facprovedor'


class Facprovtmp(models.Model):
    idfacprovedor = models.IntegerField(primary_key=True)
    idprovedor = models.IntegerField()
    idenc_mov = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    fecha_f = models.DateField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    cierre = models.DateField(blank=True, null=True)
    neto = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    ibruto = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    formap = models.IntegerField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=80, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    nograv = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    tipo_fac = models.CharField(max_length=15, blank=True, null=True)
    numero_fac = models.IntegerField(blank=True, null=True)
    letra_fac = models.CharField(max_length=1, blank=True, null=True)
    terminal_fac = models.IntegerField(blank=True, null=True)
    idprovedortmp = models.SmallIntegerField(blank=True, null=True)
    procesado = models.DateField(blank=True, null=True)
    anulado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facprovtmp'


class Facturas(models.Model):
    idfactura = models.IntegerField(primary_key=True)
    idclientesucursal = models.SmallIntegerField()
    sucursal = models.SmallIntegerField(blank=True, null=True)
    letra = models.CharField(max_length=2, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    mes = models.SmallIntegerField(blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    cierre = models.DateField(blank=True, null=True)
    neto = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    nograv = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ibrutos = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True, null=True)
    formap = models.SmallIntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    ticket = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    provincia = models.CharField(max_length=15, blank=True, null=True)
    iva = models.CharField(max_length=15, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    tipib = models.CharField(max_length=15, blank=True, null=True)
    padronib = models.CharField(max_length=10, blank=True, null=True)
    idtipmun = models.CharField(max_length=15, blank=True, null=True)
    precios = models.IntegerField(blank=True, null=True)
    conmay = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    clades = models.IntegerField(blank=True, null=True)
    flete = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivari = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivarni = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    iint = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    descfinal = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    recfinal = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ter_rem = models.IntegerField(blank=True, null=True)
    num_rem = models.IntegerField(blank=True, null=True)
    idzona = models.IntegerField(blank=True, null=True)
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idvendedor', blank=True, null=True)
    tipocob = models.IntegerField(blank=True, null=True)
    tipoope = models.CharField(max_length=4, blank=True, null=True)
    idtranspor = models.IntegerField(blank=True, null=True)
    observacion = models.BinaryField(blank=True, null=True)
    motivo = models.IntegerField(blank=True, null=True)
    sinstock = models.CharField(max_length=1, blank=True, null=True)
    regcheque = models.IntegerField(blank=True, null=True)
    xref_comp = models.CharField(max_length=15, blank=True, null=True)
    xref_let = models.CharField(max_length=1, blank=True, null=True)
    x_ref_ter = models.IntegerField(blank=True, null=True)
    x_ref_num = models.IntegerField(blank=True, null=True)
    fecped = models.DateField(blank=True, null=True)
    ocarga = models.IntegerField(blank=True, null=True)
    fecha_a = models.DateField(blank=True, null=True)
    opera_a = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=1, blank=True, null=True)
    comision = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    registro = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    ctacte = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    forcob = models.IntegerField(blank=True, null=True)
    reparto = models.CharField(max_length=2, blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)
    cae = models.CharField(max_length=15, blank=True, null=True)
    caevencimiento = models.CharField(max_length=20, blank=True, null=True)
    codigobarra = models.CharField(max_length=60, blank=True, null=True)
    dolar = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cuentaorden = models.CharField(max_length=2, blank=True, null=True)
    codigo = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'


class Familias(models.Model):
    idfamilia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familias'


class Formacobros(models.Model):
    idformacobro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    provee = models.IntegerField(blank=True, null=True)
    lista = models.IntegerField(blank=True, null=True)
    variabl = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formacobros'


class Formapagos(models.Model):
    idformapago = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    provee = models.IntegerField(blank=True, null=True)
    lista = models.IntegerField(blank=True, null=True)
    variabl = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formapagos'


class Formato(models.Model):
    comprobante = models.CharField(max_length=15, blank=True, null=True)
    copias = models.IntegerField(blank=True, null=True)
    orientacion = models.CharField(max_length=15, blank=True, null=True)
    largo = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ancho = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    encabezado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formato'


class Formatobco(models.Model):
    idformatobco = models.IntegerField(primary_key=True)
    campo = models.CharField(max_length=50, blank=True, null=True)
    desde = models.IntegerField(blank=True, null=True)
    hasta = models.IntegerField(blank=True, null=True)
    idtipfon = models.ForeignKey('Tipfon', models.DO_NOTHING, db_column='idtipfon')

    class Meta:
        managed = False
        db_table = 'formatobco'


class Hismov(models.Model):
    idhismov = models.IntegerField(primary_key=True)
    sucursal = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    detalle = models.CharField(max_length=60, blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    provincia = models.CharField(max_length=15, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    idcliente = models.IntegerField(blank=True, null=True)
    idclientesucursal = models.IntegerField(blank=True, null=True)
    conmay = models.IntegerField(blank=True, null=True)
    transpor = models.CharField(max_length=60, blank=True, null=True)
    guia = models.IntegerField(blank=True, null=True)
    otrasuc = models.IntegerField(blank=True, null=True)
    ref_let = models.CharField(max_length=1, blank=True, null=True)
    ref_ter = models.IntegerField(blank=True, null=True)
    ref_num = models.IntegerField(blank=True, null=True)
    ref_fec = models.DateField(blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)
    concilia = models.DateField(blank=True, null=True)
    deposito = models.IntegerField(blank=True, null=True)
    idprovedor = models.IntegerField(blank=True, null=True)
    bultos = models.IntegerField(blank=True, null=True)
    sueltos = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    volumen = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    flete = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    observacion = models.BinaryField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    tipcob = models.IntegerField(blank=True, null=True)
    tipope = models.CharField(max_length=15, blank=True, null=True)
    fecped = models.DateField(blank=True, null=True)
    fecha_a = models.DateField(blank=True, null=True)
    opera_a = models.IntegerField(blank=True, null=True)
    turno = models.CharField(max_length=1, blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    tipsub = models.IntegerField(blank=True, null=True)
    subcuenta = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hismov'


class ImpCta(models.Model):
    idimp_cta = models.IntegerField(primary_key=True)
    impuesto = models.CharField(max_length=15, blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imp_cta'


class Impuestos(models.Model):
    idimpuesto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    iva1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    iva2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    alicuotaafip = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impuestos'


class Iva(models.Model):
    idiva = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    alicuota = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iva'


class Lineas(models.Model):
    idlinea = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lineas'


class Listaprecios(models.Model):
    idlistaprecio = models.IntegerField(primary_key=True)
    iddet_centro = models.ForeignKey(DetCentro, models.DO_NOTHING, db_column='iddet_centro', blank=True, null=True)
    idtipoabono = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listaprecios'


class Listas(models.Model):
    idlista = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    desde = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listas'


class Localidades(models.Model):
    idlocalidad = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'localidades'


class Logcalifica(models.Model):
    idloccalifica = models.IntegerField(primary_key=True)
    idcliente = models.IntegerField(blank=True, null=True)
    idcalifica = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logcalifica'


class Marcas(models.Model):
    idmarca = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class Meses(models.Model):
    idmes = models.IntegerField(blank=True, null=True)
    mes = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meses'


class Modeloasi(models.Model):
    idmodeloasi = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modeloasi'


class Movped(models.Model):
    idmovped = models.IntegerField(primary_key=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    idstock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='idstock')
    sucursal = models.IntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    importe2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    iva = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    base = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    bonifica = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    formap = models.IntegerField(blank=True, null=True)
    ref_comp = models.CharField(max_length=15, blank=True, null=True)
    ref_num = models.IntegerField(blank=True, null=True)
    ref_comp2 = models.CharField(max_length=15, blank=True, null=True)
    ref_num2 = models.IntegerField(blank=True, null=True)
    cantped = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movped'


class Movsto(models.Model):
    idmovsto = models.IntegerField(primary_key=True)
    idstock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='idstock')
    idvendedor = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=4, blank=True, null=True)
    sucursal = models.IntegerField(blank=True, null=True)
    afecta = models.CharField(max_length=1, blank=True, null=True)
    servicio = models.CharField(max_length=1, blank=True, null=True)
    idtipocomprob = models.CharField(max_length=15, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    renglon = models.IntegerField(blank=True, null=True)
    idfamilia = models.IntegerField(blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cantcaj = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cantuni = models.IntegerField(blank=True, null=True)
    cantind = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    stock_f = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio_l = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    costo = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifc = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonife = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    canal = models.IntegerField(blank=True, null=True)
    precio_n = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    iva = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    iint = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio_f = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio_1 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    lista = models.CharField(max_length=1, blank=True, null=True)
    variabl = models.CharField(max_length=1, blank=True, null=True)
    flete = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    facflete = models.CharField(max_length=1, blank=True, null=True)
    movim = models.CharField(max_length=1, blank=True, null=True)
    rel_suc = models.IntegerField(blank=True, null=True)
    rel_comp = models.CharField(max_length=15, blank=True, null=True)
    rel_let = models.CharField(max_length=1, blank=True, null=True)
    rel_ter = models.IntegerField(blank=True, null=True)
    rel_num = models.IntegerField(blank=True, null=True)
    rel_reng = models.IntegerField(blank=True, null=True)
    ctacte = models.IntegerField(blank=True, null=True)
    codbar = models.CharField(max_length=30, blank=True, null=True)
    deposito = models.IntegerField(blank=True, null=True)
    tipope = models.CharField(max_length=4, blank=True, null=True)
    forcob = models.IntegerField(blank=True, null=True)
    aprobado = models.DateField(blank=True, null=True)
    asigna = models.DateField(blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)
    facturado = models.DateField(blank=True, null=True)
    tipoped = models.CharField(max_length=15, blank=True, null=True)
    diffec = models.DateTimeField(blank=True, null=True)
    difhora = models.CharField(max_length=10, blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    ocarga = models.IntegerField(blank=True, null=True)
    tipsub = models.IntegerField(blank=True, null=True)
    subcuenta = models.IntegerField(blank=True, null=True)
    comision = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    registro = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    idclientesucursal = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)
    percepiva = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percepib = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movsto'


class Numerosys(models.Model):
    idnumerosys = models.IntegerField(primary_key=True)
    idventa = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    nombre = models.CharField(max_length=40)
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numerosys'


class OperaComp(models.Model):
    idoperacomp = models.IntegerField(primary_key=True)
    idsubcta = models.ForeignKey('Subcta', models.DO_NOTHING, db_column='idsubcta')
    idtipo_comp = models.ForeignKey('TiposComp', models.DO_NOTHING, db_column='idtipo_comp')
    aplicable = models.CharField(max_length=1, blank=True, null=True)
    signo = models.SmallIntegerField(blank=True, null=True)
    operacion = models.SmallIntegerField(blank=True, null=True)
    libroiva = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opera_comp'


class Operacuenta(models.Model):
    idoperacuenta = models.IntegerField(primary_key=True)
    idplan = models.ForeignKey('Plancta', models.DO_NOTHING, db_column='idplan')
    idperfil = models.ForeignKey('TPerfil', models.DO_NOTHING, db_column='idperfil')

    class Meta:
        managed = False
        db_table = 'operacuenta'


class Operafondo(models.Model):
    idoperafondo = models.IntegerField(primary_key=True)
    idtipfon = models.ForeignKey('Tipfon', models.DO_NOTHING, db_column='idtipfon')
    idperfil = models.ForeignKey('TPerfil', models.DO_NOTHING, db_column='idperfil')

    class Meta:
        managed = False
        db_table = 'operafondo'


class Pagoprovedor(models.Model):
    idpagoprovedor = models.IntegerField(primary_key=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    anulado = models.DateField(blank=True, null=True)
    operaanu = models.IntegerField(blank=True, null=True)
    pagado = models.DateTimeField(blank=True, null=True)
    operapag = models.IntegerField(blank=True, null=True)
    detalle = models.CharField(max_length=80, blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagoprovedor'


class Paises(models.Model):
    idpais = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'paises'


class Paracampus(models.Model):
    idparacampus = models.IntegerField(primary_key=True)
    idplan = models.IntegerField(blank=True, null=True)
    idtipfon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paracampus'


class Parametros(models.Model):
    idparametro = models.IntegerField(primary_key=True)
    sucursal = models.IntegerField(blank=True, null=True)
    parametro = models.CharField(max_length=20, blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    puntoventa = models.SmallIntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cai = models.CharField(max_length=60, blank=True, null=True)
    copias = models.IntegerField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    comprob = models.CharField(max_length=15, blank=True, null=True)
    muevestock = models.CharField(max_length=1, blank=True, null=True)
    sepuedeanular = models.CharField(max_length=1, blank=True, null=True)
    aplica = models.CharField(max_length=1, blank=True, null=True)
    informevta = models.CharField(max_length=1, blank=True, null=True)
    tipocompafip = models.SmallIntegerField(blank=True, null=True)
    concae = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'


class Pedidos(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    codigo_cliente = models.IntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nro_vendedor = models.IntegerField(blank=True, null=True)
    datos_entrega = models.TextField(blank=True, null=True)
    datos_pedido = models.TextField(blank=True, null=True)
    rubro = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_estado = models.DateTimeField(blank=True, null=True)
    motivo_anulacion = models.TextField(blank=True, null=True)
    id_usuario = models.IntegerField(blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)
    nro_remito = models.CharField(max_length=25, blank=True, null=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    domicilio_entrega = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class PedidosDetalle(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_pedido_detalle = models.IntegerField()
    codigo_producto = models.IntegerField(blank=True, null=True)
    producto = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    original = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_detalle'
        unique_together = (('id_pedido', 'id_pedido_detalle'),)


class PedidosUsuarios(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    nro_vendedor = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True, null=True)
    band = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_usuarios'


class Pedprovedor(models.Model):
    idpedprovedor = models.IntegerField(primary_key=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    sucursal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    entrega_1 = models.DateField(blank=True, null=True)
    entrega_2 = models.DateField(blank=True, null=True)
    condicion = models.CharField(max_length=60, blank=True, null=True)
    transporte = models.CharField(max_length=60, blank=True, null=True)
    numprovedor = models.IntegerField(blank=True, null=True)
    comentario = models.BinaryField(blank=True, null=True)
    importe = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    iva = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    compro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedprovedor'


class PersSubcta(models.Model):
    idpers_subcta = models.IntegerField(primary_key=True)
    idpersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='idpersona')
    idsubcta = models.ForeignKey('Subcta', models.DO_NOTHING, db_column='idsubcta')

    class Meta:
        managed = False
        db_table = 'pers_subcta'


class Personas(models.Model):
    idpersona = models.IntegerField(primary_key=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    idruta = models.ForeignKey('Rutas', models.DO_NOTHING, db_column='idruta', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fantasia = models.CharField(max_length=50, blank=True, null=True)
    directo = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    tipope = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.SmallIntegerField(blank=True, null=True)
    letterc = models.CharField(max_length=1, blank=True, null=True)
    provincia = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    codpos = models.CharField(max_length=12, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    cheque = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    observac = models.BinaryField(blank=True, null=True)
    ctacte = models.SmallIntegerField(blank=True, null=True)
    ctacom = models.SmallIntegerField(blank=True, null=True)
    cbu = models.CharField(max_length=30, blank=True, null=True)
    cuenta = models.CharField(max_length=40, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.SmallIntegerField(blank=True, null=True)
    listaprecio = models.SmallIntegerField(blank=True, null=True)
    ingresosbruto = models.CharField(max_length=15, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    interes = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    operactacte = models.CharField(max_length=1, blank=True, null=True)
    categoriacliente = models.ForeignKey(Categoriascliente, models.DO_NOTHING, db_column='categoriacliente', blank=True, null=True)
    idiva = models.ForeignKey(Iva, models.DO_NOTHING, db_column='idiva', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Plancta(models.Model):
    idplan = models.IntegerField(primary_key=True)
    idcentro = models.ForeignKey(Centro, models.DO_NOTHING, db_column='idcentro', blank=True, null=True)
    idsubcta = models.ForeignKey('Subcta', models.DO_NOTHING, db_column='idsubcta', blank=True, null=True)
    cuenta = models.CharField(max_length=11, blank=True, null=True)
    columna = models.IntegerField(blank=True, null=True)
    item = models.IntegerField(blank=True, null=True)
    codcta = models.SmallIntegerField(blank=True, null=True)
    cod_abrev = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    asientos = models.CharField(max_length=1, blank=True, null=True)
    resultado = models.CharField(max_length=1, blank=True, null=True)
    ajuste = models.CharField(max_length=1, blank=True, null=True)
    libro = models.CharField(max_length=1, blank=True, null=True)
    fondo = models.CharField(max_length=1, blank=True, null=True)
    colres = models.IntegerField(blank=True, null=True)
    colbase = models.IntegerField(blank=True, null=True)
    porcent = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    debe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    haber = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)
    nroimagen = models.SmallIntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=1, blank=True, null=True)
    provedor = models.CharField(max_length=1, blank=True, null=True)
    codafip = models.CharField(max_length=3, blank=True, null=True)
    imponible = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plancta'


class Presup(models.Model):
    idpresup = models.IntegerField(primary_key=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    ctacte = models.IntegerField(blank=True, null=True)
    idclientesucursal = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    provincia = models.CharField(max_length=15, blank=True, null=True)
    iva = models.CharField(max_length=15, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    tipib = models.CharField(max_length=15, blank=True, null=True)
    tipmun = models.CharField(max_length=15, blank=True, null=True)
    padronib = models.CharField(max_length=15, blank=True, null=True)
    precios = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    conmay = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    descuento = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    clades = models.IntegerField(blank=True, null=True)
    neto = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    flete = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivari = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivarni = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    iint = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    nograv = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    idvendedor = models.IntegerField(blank=True, null=True)
    tipocob = models.IntegerField(blank=True, null=True)
    observac = models.BinaryField(blank=True, null=True)
    ter_oc = models.IntegerField(blank=True, null=True)
    num_oc = models.IntegerField(blank=True, null=True)
    aprobado = models.DateField(blank=True, null=True)
    asigna = models.DateField(blank=True, null=True)
    facturado = models.DateField(blank=True, null=True)
    tipped = models.CharField(max_length=15, blank=True, null=True)
    diffec = models.DateTimeField(blank=True, null=True)
    forcob = models.IntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    ocarga = models.IntegerField(blank=True, null=True)
    registro = models.IntegerField(blank=True, null=True)
    subcta = models.CharField(max_length=1, blank=True, null=True)
    proveedor = models.IntegerField(blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presup'


class Presupuesto(models.Model):
    idpresupuesto = models.IntegerField(blank=True, null=True)
    idejercicio = models.IntegerField(blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)
    iddet_centro = models.IntegerField(blank=True, null=True)
    desde = models.DateField(blank=True, null=True)
    hasta = models.DateField(blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    calculado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    incluir = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto'


class Prioridad(models.Model):
    idprioridad = models.IntegerField()
    descripcion = models.CharField(max_length=15, blank=True, null=True)
    prioridad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prioridad'


class Provctas(models.Model):
    idprovcta = models.IntegerField(primary_key=True)
    idplan = models.IntegerField(blank=True, null=True)
    idprovedor = models.ForeignKey('Provedor', models.DO_NOTHING, db_column='idprovedor')
    orden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provctas'


class Provedor(models.Model):
    idprovedor = models.IntegerField(primary_key=True)
    idprovincias = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idprovincias')
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    directo = models.CharField(max_length=1, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    tipope = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    letterc = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    localidad = models.CharField(max_length=40, blank=True, null=True)
    codpos = models.CharField(max_length=12, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    cheque = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    observacion = models.BinaryField(blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)
    ctacom = models.IntegerField(blank=True, null=True)
    directivos = models.CharField(max_length=60, blank=True, null=True)
    viajante = models.CharField(max_length=60, blank=True, null=True)
    direccion_v = models.CharField(max_length=60, blank=True, null=True)
    telefono_v = models.CharField(max_length=40, blank=True, null=True)
    tipo_ret = models.CharField(max_length=10, blank=True, null=True)
    tipo_retib = models.CharField(max_length=10, blank=True, null=True)
    padron = models.CharField(max_length=10, blank=True, null=True)
    sucursal = models.CharField(max_length=10, blank=True, null=True)
    cbu = models.CharField(max_length=30, blank=True, null=True)
    cuenta = models.CharField(max_length=40, blank=True, null=True)
    porc1 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    porc2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    porc3 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    porc4 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    viejo = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    idplancanje = models.IntegerField(blank=True, null=True)
    idclicanje = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provedor'


class Provedortmp(models.Model):
    idprovedortmp = models.IntegerField(primary_key=True)
    idprovincias = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idprovincias')
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    localidad = models.CharField(max_length=40, blank=True, null=True)
    codpos = models.CharField(max_length=12, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    tipo_ret = models.CharField(max_length=10, blank=True, null=True)
    tipo_retib = models.CharField(max_length=10, blank=True, null=True)
    padron = models.CharField(max_length=10, blank=True, null=True)
    cuenta = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provedortmp'


class Provincia(models.Model):
    idprovincias = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    dgi = models.IntegerField(blank=True, null=True)
    declara = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Provincias(models.Model):
    idprovincia = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'provincias'


class Ptovta(models.Model):
    idptovta = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    comcob1 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    diascob1 = models.SmallIntegerField(blank=True, null=True)
    comcob2 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    diascob2 = models.SmallIntegerField(blank=True, null=True)
    comvta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ptovta = models.SmallIntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    diascob3 = models.SmallIntegerField(blank=True, null=True)
    comcob3 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptovta'


class Puntosvta(models.Model):
    idpuntovta = models.CharField(primary_key=True, max_length=15)
    puntos = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntosvta'


class Remitos(models.Model):
    idremito = models.IntegerField(primary_key=True)
    sucursal = models.SmallIntegerField(blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    ctacte = models.IntegerField(blank=True, null=True)
    idclientesucursal = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    provincia = models.CharField(max_length=15, blank=True, null=True)
    iva = models.CharField(max_length=15, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    tipib = models.CharField(max_length=15, blank=True, null=True)
    tipmun = models.CharField(max_length=15, blank=True, null=True)
    padronib = models.CharField(max_length=15, blank=True, null=True)
    precios = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    conmay = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    descuento = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    clades = models.IntegerField(blank=True, null=True)
    neto = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    flete = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivari = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    ivarni = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    percep2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    iint = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    nograv = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    idvendedor = models.IntegerField(blank=True, null=True)
    tipocob = models.IntegerField(blank=True, null=True)
    observac = models.BinaryField(blank=True, null=True)
    ter_oc = models.IntegerField(blank=True, null=True)
    num_oc = models.IntegerField(blank=True, null=True)
    aprobado = models.DateField(blank=True, null=True)
    asigna = models.DateField(blank=True, null=True)
    facturado = models.DateField(blank=True, null=True)
    tipped = models.CharField(max_length=15, blank=True, null=True)
    diffec = models.DateTimeField(blank=True, null=True)
    forcob = models.IntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    ocarga = models.IntegerField(blank=True, null=True)
    faclet = models.CharField(max_length=1, blank=True, null=True)
    facter = models.IntegerField(blank=True, null=True)
    facnum = models.IntegerField(blank=True, null=True)
    deposito = models.IntegerField(blank=True, null=True)
    acopio = models.CharField(max_length=1, blank=True, null=True)
    depoa = models.IntegerField(blank=True, null=True)
    registro = models.IntegerField(blank=True, null=True)
    subcta = models.CharField(max_length=1, blank=True, null=True)
    proveedor = models.IntegerField(blank=True, null=True)
    devenga = models.IntegerField(blank=True, null=True)
    idtranspo = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.SmallIntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)
    ref_idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remitos'


class Resumen(models.Model):
    idresumen = models.IntegerField(primary_key=True)
    idtipfon = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    desde = models.SmallIntegerField(blank=True, null=True)
    hasta = models.SmallIntegerField(blank=True, null=True)
    saldoinicio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    saldofinal = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fechadesde = models.DateField(blank=True, null=True)
    cerrado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resumen'


class Retencion(models.Model):
    idretencion = models.IntegerField(primary_key=True)
    idprovedor = models.ForeignKey(Provedor, models.DO_NOTHING, db_column='idprovedor')
    sucursal = models.IntegerField(blank=True, null=True)
    tipo_pro = models.CharField(max_length=15, blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    impuesto = models.CharField(max_length=1, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    retencion = models.IntegerField(blank=True, null=True)
    imp_pag = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    imp_net = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    imp_ret = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    imp_ib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    idenc_mov = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retencion'


class Rubros(models.Model):
    idrubro = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    puntoventa = models.IntegerField(blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rubros'


class Rutas(models.Model):
    idruta = models.IntegerField(primary_key=True)
    ruta = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rutas'


class Servicios(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    idenc_mov = models.ForeignKey(EncMov, models.DO_NOTHING, db_column='idenc_mov')
    importe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    desde = models.DateField(blank=True, null=True)
    hasta = models.DateField(blank=True, null=True)
    cantpersonas = models.IntegerField(blank=True, null=True)
    cantdias = models.IntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=80, blank=True, null=True)
    idtipoabono = models.IntegerField(blank=True, null=True)
    iddet_centro = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class Sislote(models.Model):
    idsislote = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    dato1 = models.CharField(max_length=1, blank=True, null=True)
    dato2 = models.CharField(max_length=1, blank=True, null=True)
    dato3 = models.CharField(max_length=1, blank=True, null=True)
    titulo1 = models.CharField(max_length=60, blank=True, null=True)
    titulo2 = models.CharField(max_length=60, blank=True, null=True)
    titulo3 = models.CharField(max_length=60, blank=True, null=True)
    abrevia1 = models.CharField(max_length=30, blank=True, null=True)
    abrevia2 = models.CharField(max_length=30, blank=True, null=True)
    abrevia3 = models.CharField(max_length=30, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sislote'


class Stock(models.Model):
    idstock = models.IntegerField(primary_key=True)
    idsislote = models.ForeignKey(Sislote, models.DO_NOTHING, db_column='idsislote', blank=True, null=True)
    idimpuesto = models.ForeignKey(Impuestos, models.DO_NOTHING, db_column='idimpuesto', blank=True, null=True)
    iddivision = models.ForeignKey(Division, models.DO_NOTHING, db_column='iddivision', blank=True, null=True)
    idlinea = models.ForeignKey(Lineas, models.DO_NOTHING, db_column='idlinea', blank=True, null=True)
    idtipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='idtipo', blank=True, null=True)
    idfamilia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='idfamilia', blank=True, null=True)
    idmarca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='idmarca', blank=True, null=True)
    idrubro = models.ForeignKey(Rubros, models.DO_NOTHING, db_column='idrubro', blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    detalle = models.BinaryField(blank=True, null=True)
    codbarra = models.CharField(max_length=80, blank=True, null=True)
    codbarra1 = models.CharField(max_length=80, blank=True, null=True)
    servicio = models.CharField(max_length=1, blank=True, null=True)
    provedor = models.IntegerField(blank=True, null=True)
    ubicacion1 = models.CharField(max_length=4, blank=True, null=True)
    ubicacion2 = models.CharField(max_length=4, blank=True, null=True)
    ubicacion3 = models.CharField(max_length=4, blank=True, null=True)
    ubicacion4 = models.CharField(max_length=4, blank=True, null=True)
    garantia = models.IntegerField(blank=True, null=True)
    lotes = models.CharField(max_length=1, blank=True, null=True)
    costo = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    impint = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    impintp = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    usalista = models.CharField(max_length=1, blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cantuni = models.IntegerField(blank=True, null=True)
    sueltas = models.CharField(max_length=1, blank=True, null=True)
    litros = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    peso = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    volumen = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    bonifica1 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica3 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonificia4 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica5 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica6 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica7 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica8 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonifica9 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    bonificaesp = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    comivta = models.IntegerField(blank=True, null=True)
    margen = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    lista = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    descomp1 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    descomp2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    descomp3 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    descomp4 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    fechacos = models.DateField(blank=True, null=True)
    pedido = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    minimo = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    pendiente = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    lprecio = models.CharField(max_length=1, blank=True, null=True)
    cuenta = models.IntegerField(blank=True, null=True)
    provee = models.IntegerField(blank=True, null=True)
    despacho = models.CharField(max_length=30, blank=True, null=True)
    precio2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio3 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio4 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    precio5 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    comision = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    costo2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    idunidad = models.ForeignKey('Unidades', models.DO_NOTHING, db_column='idunidad')
    generico = models.CharField(max_length=1, blank=True, null=True)
    codpro = models.CharField(max_length=40, blank=True, null=True)
    tipom = models.CharField(max_length=15, blank=True, null=True)
    web = models.SmallIntegerField(blank=True, null=True)
    idclasifica = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class Stockcla(models.Model):
    idstockcla = models.IntegerField(primary_key=True)
    item = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockcla'


class Subcta(models.Model):
    idsubcta = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcta'


class TModulos(models.Model):
    idmodulo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    formulario = models.CharField(max_length=20, blank=True, null=True)
    parametro = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_modulos'


class TPerfil(models.Model):
    idperfil = models.IntegerField(primary_key=True)
    perfil = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 't_perfil'


class TPerfilusuario(models.Model):
    idperfilsuario = models.IntegerField(primary_key=True)
    t_perfil_idperfil = models.ForeignKey(TPerfil, models.DO_NOTHING, db_column='t_perfil_idperfil')
    t_usuario_idusuario = models.ForeignKey('TUsuario', models.DO_NOTHING, db_column='t_usuario_idusuario')

    class Meta:
        managed = False
        db_table = 't_perfilusuario'


class TTarea(models.Model):
    idtarea = models.IntegerField(primary_key=True)
    tarea = models.CharField(max_length=40, blank=True, null=True)
    formulario = models.CharField(max_length=40, blank=True, null=True)
    imagen = models.CharField(max_length=80, blank=True, null=True)
    icono = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tarea'


class TTareaperfil(models.Model):
    idtareaperfil = models.IntegerField(primary_key=True)
    t_perfil_idperfil = models.ForeignKey(TPerfil, models.DO_NOTHING, db_column='t_perfil_idperfil')
    t_tarea_idtarea = models.ForeignKey(TTarea, models.DO_NOTHING, db_column='t_tarea_idtarea')
    opcion = models.IntegerField(blank=True, null=True)
    item = models.IntegerField(blank=True, null=True)
    alta = models.SmallIntegerField(blank=True, null=True)
    modificar = models.SmallIntegerField(blank=True, null=True)
    borrar = models.SmallIntegerField(blank=True, null=True)
    consultar = models.SmallIntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tareaperfil'


class TUsuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    detalle = models.CharField(max_length=40, blank=True, null=True)
    clave1 = models.CharField(max_length=20, blank=True, null=True)
    mail = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_usuario'


class Tipercepcion(models.Model):
    idtipopercepcion = models.CharField(max_length=15, blank=True, null=True)
    tipocontribucion = models.CharField(max_length=1, blank=True, null=True)
    provincia = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    desde = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    hasta = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    fijo = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    porcent = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    minimo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    porcent2 = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipercepcion'


class Tipfon(models.Model):
    idtipfon = models.IntegerField(primary_key=True)
    idplan = models.ForeignKey(Plancta, models.DO_NOTHING, db_column='idplan', blank=True, null=True)
    idbanco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='idbanco', blank=True, null=True)
    moneda = models.SmallIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cartera = models.CharField(max_length=1, blank=True, null=True)
    rindea = models.IntegerField(blank=True, null=True)
    cuentabco = models.CharField(max_length=12, blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    opera = models.IntegerField(blank=True, null=True)
    codempresa = models.CharField(max_length=10, blank=True, null=True)
    datos = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipfon'


class Tipimun(models.Model):
    idtipimun = models.CharField(primary_key=True, max_length=15)
    decripcion = models.CharField(max_length=60, blank=True, null=True)
    multilateral = models.CharField(max_length=1, blank=True, null=True)
    codpostal = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipimun'


class Tipmov(models.Model):
    idtipmov = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    abrevia = models.CharField(max_length=15, blank=True, null=True)
    afecta = models.CharField(max_length=1, blank=True, null=True)
    signo = models.SmallIntegerField(blank=True, null=True)
    tipocomprob = models.CharField(max_length=15, blank=True, null=True)
    interno = models.CharField(max_length=1, blank=True, null=True)
    transferencia = models.CharField(max_length=1, blank=True, null=True)
    columna = models.IntegerField(blank=True, null=True)
    subcta = models.IntegerField(blank=True, null=True)
    parametro = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipmov'


class Tipo(models.Model):
    idtipo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo'


class Tipoingbruto(models.Model):
    idtipoingbruto = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    multilateral = models.CharField(max_length=1, blank=True, null=True)
    provincias = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoingbruto'


class Tipoiva(models.Model):
    idtipoiva = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    iva1 = models.IntegerField(blank=True, null=True)
    iva2 = models.IntegerField(blank=True, null=True)
    iint = models.IntegerField(blank=True, null=True)
    ivap = models.IntegerField(blank=True, null=True)
    letra = models.CharField(max_length=1, blank=True, null=True)
    discrimina = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoiva'


class Tiporetencion(models.Model):
    idtiporetencion = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    desde = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    hasta = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    fijo = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    minimo = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)
    retener = models.CharField(max_length=1, blank=True, null=True)
    idplan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiporetencion'


class TiposComp(models.Model):
    idtipo_comp = models.IntegerField(primary_key=True)
    abrev = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_comp'


class Tokens(models.Model):
    idtoken = models.IntegerField(primary_key=True)
    generado = models.DateField(blank=True, null=True)
    vencimiento = models.DateField(blank=True, null=True)
    token = models.CharField(max_length=2048, blank=True, null=True)
    sign = models.CharField(max_length=2048, blank=True, null=True)
    hora_gen = models.TimeField(blank=True, null=True)
    hora_ven = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'


class Transpor(models.Model):
    idtranspor = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    propio = models.CharField(max_length=1, blank=True, null=True)
    empresa = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    provincia = models.CharField(max_length=1, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    telefono1 = models.CharField(max_length=40, blank=True, null=True)
    factura = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transpor'


class Unidades(models.Model):
    idunidad = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'


class Vendedor(models.Model):
    idvendedor = models.IntegerField(primary_key=True)
    idprovincias = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='idprovincias')
    idzona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='idzona')
    nombre = models.CharField(max_length=60, blank=True, null=True)
    comentario = models.CharField(max_length=60, blank=True, null=True)
    tipcom = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    telefono1 = models.CharField(max_length=40, blank=True, null=True)
    comvta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'


class Zonas(models.Model):
    idzona = models.IntegerField(primary_key=True)
    idprovincias = models.ForeignKey(Provincia, models.DO_NOTHING, db_column='idprovincias')
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas'
