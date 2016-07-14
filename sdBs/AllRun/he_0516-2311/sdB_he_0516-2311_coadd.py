from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[79.529042,-23.145889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0516-2311/sdB_he_0516-2311_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0516-2311/sdB_he_0516-2311_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
