from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[328.631167,-9.791806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_2151-1001/sdB_he_2151-1001_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_2151-1001/sdB_he_2151-1001_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
