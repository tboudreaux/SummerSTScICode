from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[17.666875,-1.015972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_011040.05-010057.5/sdB_sdssj_011040.05-010057.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_011040.05-010057.5/sdB_sdssj_011040.05-010057.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
