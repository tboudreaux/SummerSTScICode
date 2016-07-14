from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[244.130333,0.648111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_161631.28-003853.2/sdB_SDSSJ_161631.28-003853.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_161631.28-003853.2/sdB_SDSSJ_161631.28-003853.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
