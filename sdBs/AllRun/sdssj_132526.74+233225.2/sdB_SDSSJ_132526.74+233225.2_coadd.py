from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[201.361417,23.540333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_132526.74+233225.2/sdB_SDSSJ_132526.74+233225.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_132526.74+233225.2/sdB_SDSSJ_132526.74+233225.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
