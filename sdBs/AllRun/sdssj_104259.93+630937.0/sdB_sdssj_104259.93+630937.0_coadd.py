from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.749708,63.160278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_104259.93+630937.0/sdB_sdssj_104259.93+630937.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_104259.93+630937.0/sdB_sdssj_104259.93+630937.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
