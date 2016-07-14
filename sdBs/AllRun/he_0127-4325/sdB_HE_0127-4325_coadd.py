from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[22.297667,-43.174389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_0127-4325/sdB_HE_0127-4325_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_0127-4325/sdB_HE_0127-4325_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
