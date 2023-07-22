import { db, getDoc, getDocs, doc, collection } from "./Firebase";

export const getProjects = async (props) => {
    // Specify the collection to fetch
    const collectionRef = collection(db, "user", props.user.uid, "projects");
    try {
    // Fetch the collection
    const docSnapshot = await getDocs(collectionRef);
    // Extract the documents from the collection
    // docSnapshot.docs.map((doc) => [props.setProjects(doc.data())]);
    const projectDataArray = docSnapshot.docs.map((doc) => doc.data());
    props.setProjects(projectDataArray);
    } catch (error) {
    console.error('Error fetching collection:', error);
    }
};

// Fetch user infromation from Firebase
export const getUserInfo = async (props) => {
    try {
        const docRef = doc(db, 'user',props.user.uid);
        const docSnapshot = await getDoc(docRef);
        
        if (docSnapshot.exists) {
        props.setUserInfo(docSnapshot.data());
        } else {
        console.log('Document does not exist');
        }
    } catch (error) {
        console.error('Error fetching document: ', error);
    }
};

