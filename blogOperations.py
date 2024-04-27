from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import BlogPost

blog_bp = Blueprint('blog',__name__)

# blog logic 
@blog_bp.route("/blogs", methods=["POST"])
@jwt_required()
def create_blog():
    data = request.get_json()
    author = get_jwt_identity()
    title = data.get("title")
    content = data.get("content")

    new_post = BlogPost(title=title, content=content, author=author)
    new_post.save()

    return jsonify({"message": "Blog post created successfully"}), 201
