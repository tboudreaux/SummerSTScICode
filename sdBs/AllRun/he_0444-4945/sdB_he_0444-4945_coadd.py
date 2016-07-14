from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[71.558667,-49.669667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_0444-4945/sdB_he_0444-4945_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_0444-4945/sdB_he_0444-4945_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
