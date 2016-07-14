from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[202.240583,65.33225],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_132857.74+651956.1/sdB_SDSSJ_132857.74+651956.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_132857.74+651956.1/sdB_SDSSJ_132857.74+651956.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
