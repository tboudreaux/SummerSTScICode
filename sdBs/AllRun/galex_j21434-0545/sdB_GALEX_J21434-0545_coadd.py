from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[325.859917,-5.766014],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_GALEX_J21434-0545/sdB_GALEX_J21434-0545_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_GALEX_J21434-0545/sdB_GALEX_J21434-0545_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
