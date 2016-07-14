from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[352.958167,-28.881417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_eggr_505/sdB_eggr_505_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_eggr_505/sdB_eggr_505_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
