from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[305.807625,13.21525],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_202313.83+131254.9/sdB_sdssj_202313.83+131254.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_202313.83+131254.9/sdB_sdssj_202313.83+131254.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
