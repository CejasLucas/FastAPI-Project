from app.domain.entities.document import Document


def build_documents(purchases) -> list[Document]:
    return [
        Document(
            filename=f"invoice_{i}.pdf",
            file_url=f"/documents/invoice_{i}.pdf",
            purchase_id=p.id
        )
        for i, p in enumerate(purchases, start=1)
    ]
