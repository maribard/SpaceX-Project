from user_iteration import user_iteration
from mission_stage import most_used_first_stages

from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\SpaceX Project\\foo.db'
db = SQLAlchemy(app)
#db.create_all()


class CoreModel(db.Model):
        id = db.Column(db.String(10), primary_key=True)
        reuse_count = db.Column(db.Integer, nullable=False)
        payload_mass = db.Column(db.Integer, nullable=False)

        def __repr__(self, reuse_count=None, payload_mass=None):
                return f"Core(id={id}, reuse_count={reuse_count}, payload_mass={payload_mass})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("reuse_count", type=int, help="Name of the video is required", required=True)
video_put_args.add_argument("payload_mass", type=int, help="Views of the video", required=True)

resource_fields = {
	'id': fields.String,
	'reuse_count': fields.Integer,
	'payload_mass': fields.Integer
}

class Cores(Resource):
        @marshal_with(resource_fields)
        def get(self, core_id):
                result = CoreModel.query.filter_by(id=core_id).first()
                if not result:
                        abort( 404, message="Could not find video with that id" )
                '''if not result:
                        data = trigger_fetching()
                        create_data_base(data)'''
                return result

        @marshal_with(resource_fields)
        def put(self, core_id):
                args = video_put_args.parse_args()
                '''result = CoreModel.query.filter_by( id=core_id ).first()
                print( 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' )
                if result:
                        abort( 409, message="Core id taken..." )'''

                core = CoreModel( id=core_id, reuse_count=args['reuse_count'], payload_mass=args['payload_mass'])
                db.session.add(core)
                db.session.commit()
                return core, 201


api.add_resource(Cores, "/cores/<string:core_id>")


if __name__ == "__main__":
        app.run(debug=True)



def trigger_fetching():
        dicts = {}
        lista = [('B1049', 6, 91880), ('B1051', 5, 75274), ('B1048', 4, 49245), ('B1059', 3, 23977), ('B1056', 3, 26909), ('B1046', 3, 13550), ('B1060', 2, 34680), ('B1058', 2, 24925), ('B1047', 2, 16576), ('B1052', 1, 8838), ('B1053', 1, 8838), ('B1045', 1, 2760), ('B1040', 1, 10373), ('B1043', 1, 5460), ('B1039', 1, 5670), ('B1041', 1, 19200), ('B1038', 1, 2625), ('B1025', 1, 3607), ('B1023', 1, 4450), ('B1032', 1, 4230), ('B1036', 1, 19200), ('B1035', 1, 4913), ('B1031', 1, 7690), ('B1029', 1, 13269), ('B1021', 1, 8436), ('B1063', 0, 1440), ('B1061', 0, 0), ('B1062', 0, 3681), ('B1057', 0, 2838.0), ('B1055', 0, 6000)]
        for i in lista:
                dicts[i[0]] = [i[1], i[2]]
        return dicts


def create_data_base(data):
        for key in data:
                core = CoreModel(id = key, reuse_count = data[key][0], payload_mass = data[key][1])
                db.session.add(core)
        db.session.commit()



'''print("STAGE 1")
print("Please, provide parameters")

param_a, param_b, param_c = user_iteration()

lista = most_used_first_stages(param_a, param_b, param_c)
print(lista)
lista = [('B1049', 6, 91880), ('B1051', 5, 75274), ('B1048', 4, 49245), ('B1059', 3, 23977), ('B1056', 3, 26909), ('B1046', 3, 13550), ('B1060', 2, 34680), ('B1058', 2, 24925), ('B1047', 2, 16576), ('B1052', 1, 8838), ('B1053', 1, 8838), ('B1045', 1, 2760), ('B1040', 1, 10373), ('B1043', 1, 5460), ('B1039', 1, 5670), ('B1041', 1, 19200), ('B1038', 1, 2625), ('B1025', 1, 3607), ('B1023', 1, 4450), ('B1032', 1, 4230), ('B1036', 1, 19200), ('B1035', 1, 4913), ('B1031', 1, 7690), ('B1029', 1, 13269), ('B1021', 1, 8436), ('B1063', 0, 1440), ('B1061', 0, 0), ('B1062', 0, 3681), ('B1057', 0, 2838.0), ('B1055', 0, 6000)]


for i in lista:
        print(i[0] + " " +  str(i[1]) + " " + str(i[2]))'''
