import { db, collection, setDoc, doc } from "./Firebase";
import "firebase/firestore";

export const handleAddData = async (projectName, description, purpose, consequence, deadline, userID) => {
    // Example data to be added
    const data = {
        projectName: projectName,
        description: description,
        purpose: purpose,
        consequence: consequence,
        deadline: deadline,
    };
    console.log(deadline);
    // const collectionRef = collection(db, "user", userID.uid, "projects");
    // const documentRef = doc(collectionRef);

    // await setDoc(documentRef, data);
    //   console.log("Document written with ID: ");
      
  };