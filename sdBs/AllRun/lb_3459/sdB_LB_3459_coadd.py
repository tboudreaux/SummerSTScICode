from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[82.917667,-69.884092],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LB_3459/sdB_LB_3459_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LB_3459/sdB_LB_3459_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
