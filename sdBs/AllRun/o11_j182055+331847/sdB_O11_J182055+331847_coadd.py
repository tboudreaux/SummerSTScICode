from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[275.229167,33.313056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J182055+331847/sdB_O11_J182055+331847_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J182055+331847/sdB_O11_J182055+331847_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
