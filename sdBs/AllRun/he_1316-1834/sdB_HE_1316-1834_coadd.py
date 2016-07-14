from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[199.820542,-18.831111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_1316-1834/sdB_HE_1316-1834_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_1316-1834/sdB_HE_1316-1834_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
