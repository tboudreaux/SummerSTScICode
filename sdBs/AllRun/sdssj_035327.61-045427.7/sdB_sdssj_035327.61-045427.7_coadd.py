from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[58.365042,-4.907694],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_035327.61-045427.7/sdB_sdssj_035327.61-045427.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_035327.61-045427.7/sdB_sdssj_035327.61-045427.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
