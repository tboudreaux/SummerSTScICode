from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[236.6745,6.427556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_154641.88+062539.2/sdB_sdssj_154641.88+062539.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_154641.88+062539.2/sdB_sdssj_154641.88+062539.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
